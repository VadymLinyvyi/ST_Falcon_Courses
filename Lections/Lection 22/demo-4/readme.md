migrations, db

py -m pip install flask_sqlalchemy
py -m pip install flask_migrate
py -m flask db init
py -m flask db migrate
py -m flask db upgrade

>>> from app import db
>>> from app.models import User, Post
>>> u = User(username='rekevin', email='rekevin@ukr.net')     
>>> db.session.add(u)
>>> db.session.commit()