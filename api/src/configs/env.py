from dotenv import load_dotenv
from os import environ

load_dotenv()

config = {
    'FLASK_ENV' : environ.get('FLASK_ENV'),
    'DB_HOST' : environ.get('DB_HOST'),
    'DB_NAME' : environ.get('DB_NAME'),
    'DB_USER' : environ.get('DB_USER'),
    'DB_PWD' : environ.get('DB_PWD')
}