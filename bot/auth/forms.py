from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired,Email,EqualTo, Length

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField('email', validators=[DataRequired(), Email(), Length(min=3, max=30)])
    name = StringField('name', validators=[DataRequired(), Length(min=3, max=30)])
    surname = StringField('surname', validators=[DataRequired(), Length(min=3, max=30)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=16)])