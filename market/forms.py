from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class RegisterFrom(FlaskForm):
    username = StringField(label='Username:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=Length(min=6))
    password2 = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField(label='Create Account')
    
    
    