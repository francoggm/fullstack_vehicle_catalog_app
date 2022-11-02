from flask import request, jsonify, Blueprint, make_response
from datetime import timedelta, datetime
import uuid
import jwt

from . import app, db
from .models import User

#Authentication
auth = Blueprint('auth', __name__, url_prefix='/auth')

def generate_token(payload, exp=datetime.utcnow() + timedelta(minutes=20)):
    if isinstance(payload, dict):
        payload.update({"exp": exp})
        return jwt.encode(payload, app.secret_key)

@auth.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if data.get('name') and data.get('email') and data.get('password'):
            user = User(name = data['name'], email = data['email'], password = data['password'], public_id=str(uuid.uuid4()))
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "User has been registered"})
        return make_response(jsonify({"message": "Error creating new user, missing informations"}), 406)
    except:
        return make_response(jsonify({"message": "Error creating new user, try again"}))

@auth.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if data.get('email') and data.get('password'):
            user = User.query.filter_by(email=data['email']).first()
            if user:
                if user.check_password_hash(data['password']):
                    token = generate_token({"public_id": user.public_id})
                    print(token)
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
            if datetime.now() + timedelta(minutes=8) >= exp:
                new_token = generate_token({"public_id": user.public_id})
                return make_response(jsonify({"token": new_token.decode('UTF-8')}), 200)
            return make_response(jsonify({"message": ""}), 425)
        else:
            return make_response(jsonify({"message": "Invalid user"}), 401)
    except:
        return make_response(jsonify({"message": "Invalid token"}), 401)
