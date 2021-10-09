from dotenv import load_dotenv
from os import environ
from flask.app import Flask

load_dotenv()

config = {
    'DB_HOST' : environ.get('DB_HOST'),
    'DB_NAME' : environ.get('DB_NAME'),
    'DB_USER' : environ.get('DB_USER'),
    'DB_PWD' : environ.get('DB_PWD')
}

def init_app(app: Flask):

    app.config['FLASK_ENV'] = environ.get('FLASK_ENV')
    app.config['JSON_SORT_KEYS'] = False