from flask import Flask
from dotenv import load_dotenv
from os import environ

load_dotenv()

def init_app(app: Flask):
    app.config['FLASK_ENV'] = environ.get('FLASK_ENV')
    app.config['DB_HOST'] = environ.get('DB_HOST')
    app.config['DB_NAME'] = environ.get('DB_NAME')
    app.config['DB_USER'] = environ.get('DB_USER')
    app.config['DB_PWD'] = environ.get('DB_PWD')