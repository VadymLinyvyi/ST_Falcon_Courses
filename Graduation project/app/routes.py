# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect, url_for
from app import app
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User


nav = Nav(app)
nav.register_element(
    "main_menu_bar",
    Navbar(
        "menu_bar",
        View('Автосервіс "Роги і копита"', 'index'),
        View('Ввійти', 'login'),
        Subgroup(
            'Про компанію',
            View('Історія', 'history'),
            View('Програма SOS – Sправжня Опіка Sервісу', 'sos_program'),
            View('Вакансії', 'vacancies'),
            View('Контакти', 'contacts'),
            View('Відгуки', 'reviews')
        ),
        Subgroup(
            'Автосервіс',
            View('Записатись на сервіс', 'service'),
            View('Кузовний ремонт', 'service'),
            View('Запчастини', 'service'),
            View('Аксесуари для автомобілів', 'service'),
            View('Вартість технічного обслуговування', 'service'),
            View('Програма лояльності', 'service'),
            View('Корпоративним клієнтам', 'service')
        ),
        Subgroup(
            'Прес-центр',
            View('Новини', 'press'),
            View('Акції', 'press')
        )
    )
)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='СТО')


@app.route('/about')
def about():
    return "pass"


@app.route('/service')
def service():
    return 'pass'


@app.route('/press')
def press():
    return 'pass'


@app.route('/history')
def history():
    return 'pass'


@app.route('/sos_program')
def sos_program():
    return 'pass'


@app.route('/vacancies')
def vacancies():
    return 'pass'


@app.route('/contacts')
def contacts():
    return 'pass'


@app.route('/reviews')
def reviews():
    user = {'username': 'User1'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('reviews.html', title='Відгуки', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Невірне ім'я користувача чи пароль")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Авторизація', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))
