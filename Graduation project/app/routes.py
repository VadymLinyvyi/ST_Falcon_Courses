# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    main_menu = [
        {
            'Text': 'Автосервіс "Роги і копита"',
            'url': 'index'
        },
        {
            'Text': 'Про компанію',
            'url': 'about'
        },
        {
            'Text': 'Автосервіс',
            'url': 'service'
        },
        {
            'Text': 'Прес-центр',
            'url': 'press'
        }
    ]
    return render_template('index.html', title='СТО', main_menu=main_menu)


@app.route('/about')
def about():
    return "pass"


@app.route('/service')
def service():
    return 'pass'


@app.route('/press')
def press():
    return 'pass'
