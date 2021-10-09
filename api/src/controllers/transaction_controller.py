from flask import request, jsonify, current_app
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
            return {'msg': 'You need to upload a file'}, 400
        try:
            binary_file = cls.get_file_data(file)
            if not binary_file:
                return {'msg': 'Invalid file'}, 400
            cls.check_file(binary_file)
            rows = cls.split_file_to_rows(binary_file)
            return TransactionModel.register(rows)

        except (InvalidCNABFile) as e:
            return e.msg, e.status
        except (UnicodeDecodeError) as e:
            return {'msg': 'Invalid file'}, 400