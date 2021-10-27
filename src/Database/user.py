from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    
    id    = db.Column(db.Integer, primary_key=True)

    login = db.Column(db.String())
    username = db.Column(db.String())

    password = db.Column(db.String())
    token = db.Column(db.String())

    def serialize(self):
        return {
            'id': self.id,
            'login': self.login,
            'username': self.username,
            'token': self.token
        }

    pass