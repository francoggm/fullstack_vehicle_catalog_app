from datetime import datetime, timedelta
from flask import jsonify

from . import app, db
from .models import User
from .token import token_required

#Users handler - just ADMIN
@app.route('/user/<public_id>', methods=['GET'])
@token_required
def get_user(current_user, public_id):
    try:
        if not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        user = User.query.filter_by(public_id=public_id).first()
        if user:
            output = {"name": user.name, "email": user.email, "password": user.password, "admin": user.admin,"public_id": user.public_id}
            return jsonify({"user": output})
        return jsonify({"message": "Error getting user, no user found"})
    except:
        return jsonify({"message": "Error getting user, try again"})

@app.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    try:
        if not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        users = User.query.all()
        if users:
            output = [{"name": user.name, "email": user.email, "password": user.password, "admin": user.admin,"public_id": user.public_id} for user in users]
            return jsonify({"users": output})
        return jsonify({"message": "Error getting all users, no users found"})
    except:
        return jsonify({"message": "Error getting all users, try again"})

@app.route('/user/<public_id>', methods=['DELETE'])
@token_required
def delete_user(current_user, public_id):
    try:
        if not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        user = User.query.filter_by(public_id=public_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User has been deleted"})
        return jsonify({"message": "Error deleting user, no users found"})
    except:
        return jsonify({"message": "Error deleting user, try again"})

@app.route('/user', methods=['DELETE'])
@token_required
def delete_all_users(current_user):
    try:
        if not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

        users = User.query.all()
        for user in users:
            db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "All users has been deleted"})
    except:
        return jsonify({"message": "Error deleting all users, try again"})

@app.route('/user/<public_id>', methods=['PUT'])
@token_required
def promote_user_admin(current_user, public_id):
    if not current_user.admin:
            return jsonify({"message": "You do not have permission to do that"})

    user = User.query.filter_by(public_id=public_id).first()
    if user:
        user.admin = True
        db.session.commit()
        return jsonify({"message": "User has been promoted to admin"})
    return jsonify({"message": "Error promoting user, no user found"})



