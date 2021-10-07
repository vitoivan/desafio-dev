from datetime import datetime
from .database_model import Database
from psycopg2 import sql
import psycopg2

class TransactionModel:
    
    types = {
        1: 'Débito',
        2: 'Boleto',
        3: 'Crédito',
        4: 'Crédito',
        5: 'Recebimento Empréstimo',
        6: 'Vendas',
        7: 'Recebimento TED',
        8: 'Recebimento DOC',
        9: 'Alugel'
    }

    @staticmethod
    def normalize_row(row: str):
        return {
            'type' : TransactionModel.types[int(row[0])],
            'date' : datetime.date(datetime.strptime(row[1:9], '%Y%m%d')),
            'value' : float(int(row[9:19])/100.0),
            'cpf' : row[19:30],
            'card' : row[30:42],
            'time' : datetime.time(datetime.strptime(row[42:48], '%H%M%S')),
            'owner_name' : row[48:62].strip(),
            'shop_name' : row[62:].strip()
        }

    @classmethod
    def register(cls, rows: list[str], app):
        
        db = Database(app)

        for row in rows:
            data = cls.normalize_row(row)
            cls.register_owner(app, str(data['owner_name']))
            cls.register_shop(app, str(data['shop_name']))

        return 'ok'
    
    @staticmethod
    def register_owner(app , owner_name):
        
        db = Database(app)
        query = sql.SQL("""
        INSERT INTO donos
            (nome)
        VALUES
            ({owner});
        """).format(owner=sql.Literal(owner_name))
        try:
            db.cur.execute(query)
            db.conn.commit()
        except psycopg2.errors.UniqueViolation as e:
            db.close()


    def register_shop(app , shop_name):
        
        db = Database(app)
        query = sql.SQL("""
        INSERT INTO lojas
            (nome)
        VALUES
            ({shop});
        """).format(shop=sql.Literal(shop_name))
        try:
            db.cur.execute(query)
            db.conn.commit()
        except psycopg2.errors.UniqueViolation as e:
            db.close()

        