from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,EqualTo,Length,ValidationError

from models import User

class RegistrationForm(FlaskForm):
    username=StringField('username',validators=[
        InputRequired(message='username required'),
        Length(min=4,max=20,message='username must be between 4 and 80 character')])
    password=PasswordField('password',validators=[
        InputRequired(message='password required'),
        Length(min=4,max=20,message='username must be between 4 and 20 character')])
    confirm_password=PasswordField('confirm_password',validators=[
        InputRequired(message='password required'),
        EqualTo('password',message='passwords must match')])
    submit=SubmitField('submit')


    def validate_username(self,username):
        user_d=User.query.filter_by(username=username.data).first()
        if(user_d):
            raise ValidationError('Username already exixts select a different username')


class LoginForm(FlaskForm):
    username=StringField('username',validators=[InputRequired(message='username required')])
    password=PasswordField('password',validators=[InputRequired(message='password required')])
    submit=SubmitField('submit')

    def validate_username(self,username):
        user_d=User.query.filter_by(username=username.data).first()
        if(user_d==None):
            raise ValidationError('this username does not exixts')

