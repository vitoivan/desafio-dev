import psycopg2

class Database:

    def __init__(self, app):
        host = app.config['DB_HOST']
        name = app.config['DB_NAME']
        user = app.config['DB_USER']
        pwd = app.config['DB_PWD']

        self.conn = psycopg2.connect(
            host=host,
            database=name,
            user=user,
            pwd=pwd
        )
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()