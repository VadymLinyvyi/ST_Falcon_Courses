from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class EditProfileForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    about_me = TextAreaField('Про мене', validators=[Length(min=0, max=140)])
    submit = SubmitField('Підтвердити')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError("Виберіть інше ім'я")


class LoginForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField("Запам'ятати")
    submit = SubmitField('Ввійти')


class RegistrationForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторіть пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватись')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Виберіть, будь-ласка, інше ім'я")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Виберіть, будь-ласка, інший e-mail")


class PostForm(FlaskForm):
    post = TextAreaField('Залиште відгук', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Підтвердити')
