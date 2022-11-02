from functools import wraps
from flask import request, jsonify, make_response
import jwt

from . import app
from .models import User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            
        if not token:
            return jsonify({"message": "Token is missing, verify headers"})
        try:
            data = jwt.decode(token, app.secret_key)
            user = User.query.filter_by(public_id=data['public_id']).first()
        except:
            return make_response(jsonify({"message": "Invalid token"}), 401)
        return f(user, *args, **kwargs)
    return decorated