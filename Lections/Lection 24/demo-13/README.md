Language/Translations

export FLASK_DEBUG=0

pip install flask-babel

py -m flask db init
py -m flask db migrate
py -m flask db upgrade

py -m flask run

https://pythonhosted.org/Flask-Babel/