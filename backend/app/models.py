from sqlalchemy.sql import func
from werkzeug.security import check_password_hash, generate_password_hash

from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    _password = db.Column(db.String(250), nullable=False)
    admin = db.Column(db.Boolean(), default=False)
    register_date = db.Column(db.DateTime(timezone=True), default=func.now())

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password, method='sha256')
    
    def check_password_hash(self, password) -> bool:
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f'{self.name} - {self.public_id}'

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    register_date = db.Column(db.DateTime(timezone=True), default=func.now())

    def __repr__(self) -> str:
        return f'{self.name} - {self.brand}'

