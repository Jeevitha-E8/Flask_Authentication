import email
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

from myauthproject.models import User

class LoginForm(FlaskForm):
    email = StringField('Enter your Email: ',validators=[DataRequired(), Email()])
    password = StringField('Enter your Password: ',validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    username = StringField('UserName: ',validators=[DataRequired()])
    email = StringField('Email: ',validators=[DataRequired(),Email()]) 
    password = PasswordField('Password: ',validators=[DataRequired(),EqualTo('chkn_password',message='Passwords should match!')])
    chkn_password = PasswordField('Confirm Password: ',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Email has been registered')
    def validate_username(self, username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username has been registered')