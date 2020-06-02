Email

export FLASK_DEBUG=0

py -m pip install flask-mail
py -m pip install pyjwt

export MAIL_SERVER=localhost
export MAIL_PORT=8025

py -m smtpd -n -c DebuggingServer localhost:8025

py -m flask db init
py -m flask db migrate
py -m flask db upgrade

py -m flask run