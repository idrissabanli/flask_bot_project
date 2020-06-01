from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms.validators import DataRequired,Email,EqualTo, Length
from .models import check_username_model, check_email_model
from wtforms.widgets import PasswordInput

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField('Password', widget=PasswordInput(hide_value=False), validators=[DataRequired(), Length(min=8, max=16)])


class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(min=3, max=30)])
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=30)])
    surname = StringField('surname', validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField('password',  validators=[DataRequired(), Length(min=8, max=16)])

    def validate_username(self, field):
        if check_username_model(field.data):
            raise ValidationError('Username already taken')
        else:
            return field
    
    def validate_email(self, field):
        if check_email_model(field.data):
            raise ValidationError('Email already taken')
        else:
            return field