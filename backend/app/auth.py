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
        return jsonify({"message": "Error creating new user, missing informations"})
    except:
        return jsonify({"message": "Error creating new user, try again"})

@auth.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    if data.get('email') and data.get('password'):
        user = User.query.filter_by(email=data['email']).first()
        if user:
            if user.check_password_hash(data['password']):
                token = generate_token({"public_id": user.public_id})
                return jsonify({"token": token.decode('UTF-8')})
            return jsonify({"message": "Error logging, wrong password!"})
        return jsonify({"message": "Error logging, email not found!"})
    return jsonify({"message": "Error logging, missing informations!"})

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
            if datetime.now() + timedelta(minutes=5) >= exp:
                new_token = generate_token({"public_id": user.public_id})
                return make_response(jsonify({"token": new_token.decode('UTF-8')}), 200)
            return make_response(jsonify({"message": ""}), 425)
        else:
            return make_response(jsonify({"message": "Invalid user"}), 401)
    except:
        return make_response(jsonify({"message": "Invalid token"}), 401)
