from datetime import datetime, timedelta
from flask import jsonify, Blueprint

from . import db
from .models import User
from .token import token_required

users = Blueprint('users', __name__)

# Users handler - just ADMIN
@users.before_request
@token_required
def before_request(current_user):
    if not current_user or not current_user.admin:
        return jsonify({"message": "You do not have permission to do that"}), 401

@users.route('/user/<public_id>', methods=['GET'])
def get_user(public_id):
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if user:
            output = {"name": user.name, "email": user.email, "password": user.password, "admin": user.admin,"public_id": user.public_id}
            return jsonify({"user": output}), 200
        return jsonify({"message": "Error getting user, no user found"}), 404
    except:
        return jsonify({"message": "Error getting user, try again"}), 400

@users.route('/user', methods=['GET'])
def get_all_users():
    try:
        users = User.query.all()
        if users:
            output = [{"name": user.name, "email": user.email, "password": user.password, "admin": user.admin,"public_id": user.public_id} for user in users]
            return jsonify({"users": output}), 200
        return jsonify({"message": "Error getting all users, no users found"}), 404
    except:
        return jsonify({"message": "Error getting all users, try again"}), 400

@users.route('/user/<public_id>', methods=['DELETE'])
def delete_user(public_id):
    try:
        user = User.query.filter_by(public_id=public_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User has been deleted"}), 200
        return jsonify({"message": "Error deleting user, no users found"}), 404
    except:
        return jsonify({"message": "Error deleting user, try again"}), 400

@users.route('/user', methods=['DELETE'])
def delete_all_users():
    try:
        users = User.query.all()
        for user in users:
            db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "All users has been deleted"}), 200
    except:
        return jsonify({"message": "Error deleting all users, try again"}), 400

@users.route('/user/<public_id>', methods=['PUT'])
def promote_user_admin(public_id):
    user = User.query.filter_by(public_id=public_id).first()
    if user:
        if not user.admin:
            user.admin = True
            db.session.commit()
            return jsonify({"message": "User has been promoted to admin"}), 200
        return jsonify({"message": "User already is admin"}), 400
    return jsonify({"message": "Error promoting user, no user found"}), 404



