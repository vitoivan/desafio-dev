from flask import request
from flask.json import jsonify
from src.models.errors import  InvalidCNABFile
from src.models.transaction_model import TransactionModel
import re

class TransactionController:

    @staticmethod
    def check_line(row: str):
        reg = r"([1-9])(\d{33})(\*{4})(\d{10})(.{32,34})"
        if re.fullmatch(reg, row) == None:
            raise InvalidCNABFile()
    
    @staticmethod
    def split_file_to_rows(file):
        rows = []
        line = ''
        for letter in file:
            if letter != '\n':
                line += letter
            else:
                rows.append(line)
                line = ''
        return rows

    @staticmethod
    def get_file_data(file):

        for key, value in file.items():
            binary = value.read()
            binary = binary.decode()
            value.seek(0)
            return binary


    @classmethod
    def check_file(cls, binary_file):

        rows = cls.split_file_to_rows(binary_file)
        for row in rows:
            cls.check_line(row)
             
    
    @classmethod
    def post(cls):
        
        file = request.files
        if len(file) == 0:
            return jsonify({'msg': 'You need to upload a file'}), 400
        try:
            binary_file = cls.get_file_data(file)
            if not binary_file:
                return jsonify({'msg': 'Invalid file'}), 400
            cls.check_file(binary_file)
            rows = cls.split_file_to_rows(binary_file)
            return jsonify(TransactionModel.register(rows)), 201
        
        except (InvalidCNABFile) as e:
            return jsonify(e.msg), e.status
        except (UnicodeDecodeError) as e:
            return jsonify({'msg': 'Invalid file'}), 400

    @staticmethod
    def normalize(transaction):
        return {
            'id': transaction[0],
            'type': transaction[1],
            'date': transaction[2].strftime("%Y-%m-%d"),
            'value': transaction[3],
            'cpf': transaction[4],
            'card': transaction[5],
            'hour': transaction[6].strftime("%H-%M-%S"),
            'owner': transaction[7],
            'shop': transaction[8]
        }
    @classmethod
    def get(cls):
        #perpage e pagenumber
        per_page = request.args.get('perpage')
        page_number = request.args.get('pagenumber')

       
        if (not per_page) or (not page_number):
            return jsonify({'msg': 'Invalid query parameters'}), 400
        
        transactions = TransactionModel.get_transactions(int(per_page), int(page_number))
        return jsonify([cls.normalize(t) for t in transactions]), 200