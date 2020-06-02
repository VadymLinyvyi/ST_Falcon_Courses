Elasticsearch 

export FLASK_DEBUG=0

pip install elasticsearch

py -m flask db init
py -m flask db migrate
py -m flask db upgrade

py -m flask run