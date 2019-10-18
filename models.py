from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db=SQLAlchemy()

class User(UserMixin,db.Model):
    '''user model'''
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"




