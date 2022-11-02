from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
import uuid

def create_db():
    db_name = app.config['DATABASE_URI'].split('/')[-1]
    if not db_name in os.listdir(os.getcwd()):
        db.create_all()
        # admin = User(name="admin", email="admin@admin.com", password="12345", admin=True, public_id=str(uuid.uuid4()))
        # db.session.add(admin)
        # db.session.commit()

app = Flask(__name__)
cors = CORS(app)

app.config.from_pyfile('../config.py')
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = app.config['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from .models import User, Vehicle

create_db()

from .auth import auth
from .users import users
from .routes import routes

app.register_blueprint(auth)
app.register_blueprint(users)
app.register_blueprint(routes)



