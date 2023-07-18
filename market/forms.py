from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, TextAreaField

class RegisterFrom(FlaskForm):
    username = StringField(label='Username:')
    email_address = StringField(label='Email Address:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Confirm Password:')
    submit = SubmitField(label='Create Account')
    
    
    