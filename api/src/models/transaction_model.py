from datetime import datetime
from psycopg2.errors import UniqueViolation
from .database_model import Database
from psycopg2 import sql

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
    def register(cls, rows: list[str]):
        
        db = Database()

        for row in rows:
            data = cls.normalize_row(row)
            cls.register_owner(db, data['owner_name'])
        return 'ok'
    
    @staticmethod
    def register_owner(db, owner_name):

        query = sql.SQL("""
            INSERT INTO donos
                (nome)
            VALUES
                ({owner});
        """).format(owner=sql.Literal(owner_name))
        db.cur.execute(query)
        db.conn.commit()

