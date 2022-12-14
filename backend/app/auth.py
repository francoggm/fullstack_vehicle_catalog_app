from flask import request, jsonify, Blueprint, make_response
from datetime import timedelta, datetime
import uuid
import jwt

from . import app, db
from .models import User

#Authentication
auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if data.get('name') and data.get('email') and data.get('password'):
            user = User(name = data['name'], email = data['email'], password = data['password'], public_id=str(uuid.uuid4()))
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User has been registered"}), 200
        return make_response(jsonify({"message": "Error creating new user, missing informations"}), 406)
    except:
        return make_response(jsonify({"message": "Error creating new user, try again"}), 400)

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if data.get('email') and data.get('password'):
            user = User.query.filter_by(email=data['email']).first()
            if user:
                if user.check_password_hash(data['password']):
                    payload = {"public_id": user.public_id, "exp": datetime.utcnow() + timedelta(minutes=20)}
                    token = jwt.encode(payload, app.secret_key)
                    return make_response(jsonify({"token": token.decode('UTF-8'), "admin": user.admin}), 200)
                return make_response(jsonify({"message": "Error logging, wrong password!"}), 404)
            return make_response(jsonify({"message": "Error logging, email not found!"}), 404)
        return make_response(jsonify({"message": "Error logging, missing informations!"}), 406)
    except:
        return make_response(jsonify({"message": "Error logging, try again"}), 406)

@auth.route('/refresh_token', methods=['GET'])
def refresh_token():
    if not 'x-access-token' in request.headers:
        return jsonify({"message": "Token is missing, verify headers"})
    token = request.headers['x-access-token']
    try:
        data = jwt.decode(token, app.secret_key)
        user = User.query.filter_by(public_id=data['public_id']).first()
        if user:
            exp = datetime.fromtimestamp(data['exp'])
            if datetime.utcnow() + timedelta(minutes=5) >= exp:
                payload = {"public_id": user.public_id, "exp": datetime.utcnow() + timedelta(minutes=20)}
                new_token = jwt.encode(payload, app.secret_key)
                return make_response(jsonify({"token": new_token.decode('UTF-8')}), 200)
            return make_response(jsonify({"message": ""}), 425)
        else:
            return make_response(jsonify({"message": "Invalid user"}), 401)
    except:
        return make_response(jsonify({"message": "Invalid token"}), 401)
