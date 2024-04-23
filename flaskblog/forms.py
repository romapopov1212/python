from flask_wtf import FlaskForm
from flask_wtf .file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 2, max = 40)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit_Field = SubmitField("Sign up")
    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError("This username is taken. Please choose another")
    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError("This email is taken. Please choose another")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit_Field = SubmitField("Login")
    remember = BooleanField("Remember me")


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError("This username is taken. Please choose another")
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError("This email is taken. Please choose another")
            
class PostForm(FlaskForm):
    title = StringField("Title", validators= [DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField("Post")

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError("There is no account with that email. You must register new")
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Password Reset')
        
