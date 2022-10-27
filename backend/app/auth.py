from flask import request, jsonify
from datetime import timedelta, datetime
import uuid
import jwt

from . import app, db
from .models import User

#Authentication
@app.route('/register', methods=['POST'])
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

@app.route('/login', methods=['GET'])
def login():
    data = request.get_json()
    if data.get('email') and data.get('password'):
        user = User.query.filter_by(email=data['email']).first()
        if user:
            if user.check_password_hash(data['password']):
                exp = datetime.utcnow() + timedelta(hours=12)
                token = jwt.encode({"public_id": user.public_id, "exp": exp}, app.secret_key)
                return jsonify({"token": token.decode('UTF-8')})
            return jsonify({"message": "Error logging, wrong password!"})
        return jsonify({"message": "Error logging, email not found!"})
    return jsonify({"message": "Error logging, missing informations!"})