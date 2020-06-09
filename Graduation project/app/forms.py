from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from flask_babel import _
from flask_babel import lazy_gettext as _l


class EditProfileForm(FlaskForm):
    username = StringField(_l("Ім'я користувача"), validators=[DataRequired()])
    about_me = TextAreaField(_l('Про мене'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Підтвердити'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l("Виберіть інше ім'я"))


class LoginForm(FlaskForm):
    username = StringField(_l("Ім'я користувача"), validators=[DataRequired()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    remember_me = BooleanField(_l("Запам'ятати"))
    submit = SubmitField(_l('Ввійти'))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Ім'я користувача"), validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField(_l('Пароль'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторіть пароль'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Зареєструватись'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l("Виберіть, будь-ласка, інше ім'я"))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l("Виберіть, будь-ласка, інший e-mail"))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Залиште відгук'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Підтвердити'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Відновити пароль'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Введіть новий пароль'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Повторіть новий пароль'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Змінити пароль'))
