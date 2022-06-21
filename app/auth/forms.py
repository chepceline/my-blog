from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField, FileField
from wtforms.validators import DataRequired,Email,Length,EqualTo
from ..models import User
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(),Email()])
    password = PasswordField(validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')


class SignUpForm(FlaskForm):
    email = StringField('Email Address', validators=[DataRequired(), Email()])
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Passwords do not match.')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    profile = FileField('Upload Profile Picture', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images only allowed.')])
    sub = BooleanField('Subscribe to receive updates about new posts.')
    submit = SubmitField('Sign Up')

    # Validate email
    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email has an existing account.')

    # Validate username
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username is taken.')