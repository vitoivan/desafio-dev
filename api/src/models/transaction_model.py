from datetime import datetime
from .database_model import Database
from psycopg2 import sql
import psycopg2
from flask import jsonify

class TransactionModel:
    
    types = {
        '1': 'Débito',
        '2': 'Boleto',
        '3': 'Crédito',
        '4': 'Crédito',
        '5': 'Recebimento Empréstimo',
        '6': 'Vendas',
        '7': 'Recebimento TED',
        '8': 'Recebimento DOC',
        '9': 'Aluguel'
    }

    @staticmethod
    def normalize_row(row: str):
        return {
            'type' : TransactionModel.types[str(row[0])],
            'date' : datetime.date(datetime.strptime(row[1:9], '%Y%m%d')),
            'value' : float(int(row[9:19])/100.0),
            'cpf' : row[19:30],
            'card' : row[30:42],
            'time' : datetime.time(datetime.strptime(row[42:48], '%H%M%S')),
            'owner_name' : row[48:62].strip(),
            'shop_name' : row[62:].strip()
        }
        
    @classmethod
    def register(cls, rows: list):
        
        output = []
        for row in rows:
            data = cls.normalize_row(row)
            cls.register_owner(str(data['owner_name']))
            cls.register_shop(str(data['shop_name']))
            output.append(cls.register_transaction(data))
            
        return output
    
    @staticmethod
    def register_owner(owner_name):
        
        db = Database()
        query = sql.SQL("""
        INSERT INTO donos
            (nome)
        VALUES
            ({owner});
        """).format(owner=sql.Literal(owner_name))
        try:
            db.cur.execute(query)
            db.conn.commit()
            db.close()
        except psycopg2.errors.UniqueViolation as e:
            db.close()


    def register_shop(shop_name):
        
        db = Database()
        query = sql.SQL("""
        INSERT INTO lojas
            (nome)
        VALUES
            ({shop});
        """).format(shop=sql.Literal(shop_name))
        try:
            db.cur.execute(query)
            db.conn.commit()
            db.close()
        except psycopg2.errors.UniqueViolation as e:
            db.close()

        
    def get_owner(name = None):
        
        db = Database()
        if name == None:
            query = sql.SQL("""SELECT * FROM donos;""")
           
        else:
            query = sql.SQL("""
                SELECT * FROM donos WHERE nome = {name};
            """).format(name=sql.Literal(name))
        
        db.cur.execute(query)
        data = db.cur.fetchall()
        db.close()
        return data

    def get_shop(name = None):
        
        db = Database()
        if name == None:
            query = sql.SQL("""SELECT * FROM lojas;""")
           
        else:
            query = sql.SQL("""
                SELECT * FROM lojas WHERE nome = {name};
            """).format(name=sql.Literal(name))
        
        db.cur.execute(query)
        data = db.cur.fetchall()
        db.close()
        return data


    def get_type(type_name = None):
        
        db = Database()
        if type_name == None:
            query = sql.SQL("""SELECT * FROM tipos;""")
            db.cur.execute(query)
            data = db.cur.fetchall()
        
        else:
            query = sql.SQL("""
                SELECT * FROM tipos WHERE nome = {type_name};
            """).format(type_name=sql.Literal(type_name))
            db.cur.execute(query)
            data = db.cur.fetchone()
 
        db.close()
        return data

    @classmethod
    def register_transaction(cls, data):
    
        db = Database()

        type = cls.get_type(data['type'])
        owner = cls.get_owner(data['owner_name'])
        shop = cls.get_shop(data['shop_name'])
        query = sql.SQL("""
            INSERT INTO transacoes 
            (tipo_id, data, valor, cpf, cartao, hora, id_dono, id_loja)
            VALUES
                (
                    {type},
                    {date},
                    {value},
                    {cpf},
                    {card},
                    {hour},
                    {id_dono},
                    {id_shop}
                ) 
            RETURNING *;
        """).format(
            type=sql.Literal(type[0]),
            date=sql.Literal(data['date']),
            value=sql.Literal(data['value']),
            cpf=sql.Literal(data['cpf']),
            card=sql.Literal(data['card']),
            hour=sql.Literal(data['time']),
            id_dono=sql.Literal(owner[0][0]),
            id_shop=sql.Literal(shop[0][0]),
        )
        db.cur.execute(query)
        db.conn.commit()
        data = db.cur.fetchall()[0]
        db.close()
        if len(data) > 0:
            return {
                'id': data[0],
                'type': type[1],
                'date': data[2].strftime("%Y-%m-%d"),
                'value': data[3],
                'cpf': data[4],
                'card': data[5],
                'time': data[6].strftime("%H-%M-%S"),
                'owner': owner[0][1],
                'shop': shop[0][1],
            }
        return []

    @staticmethod
    def get_transactions(per_page: int, page_number: int):

        db = Database()
        offset = per_page * (page_number - 1)
        query = sql.SQL("""
            SELECT 
                tr.id, t.nome, tr.data, tr.valor, tr.cpf, tr.cartao, tr.hora, d.nome, l.nome 
            FROM 
                transacoes tr 
            JOIN tipos t 
                ON t.id = tr.tipo_id 
            JOIN donos d 
                ON d.id = tr.id_dono
            JOIN lojas l 
                ON l.id = tr.id_loja 
            LIMIT {per} OFFSET {off};
        """).format(
            per=sql.Literal(per_page),
            off=sql.Literal(offset))
        db.cur.execute(query)
        data = db.cur.fetchall()
        db.close()
        return data