from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,EqualTo,Length,ValidationError
from passlib.hash import pbkdf2_sha256
from models import User

"""inline custom validator"""
def invalid_credential(form,fields):
    entered_username=form.username.data
    entered_password=fields.data

    user_d=User.query.filter_by(username=entered_username).first()
    if(user_d is None):
        raise ValidationError('Username or password is incorrect')
    elif not pbkdf2_sha256.verify(entered_password, user_d.password):
        raise ValidationError('Username or password is incorrect')


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
    password=PasswordField('password',validators=[InputRequired(message='password required'),
        invalid_credential])
    submit=SubmitField('login')



