import psycopg2
from src.configs.env import config

class Database:

    def __init__(self):
        host = config['DB_HOST']
        name = config['DB_NAME']
        user = config['DB_USER']
        pwd =  config['DB_PWD']

        try:
            self.conn = psycopg2.connect(
                host=host,
                database=name,
                user=user,
                password=pwd
            )
        except psycopg2.OperationalError as e:
            self.conn = psycopg2.connect(
                host='localhost',
                database=name,
                user=user,
                password=pwd
            )
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()