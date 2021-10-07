from flask import request, jsonify
from src.models.errors import InvalidFileType, InvalidCNABFile
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
            if chr(letter) != '\n':
                line += chr(letter)
            else:
                rows.append(line)
                line = ''
        return rows

    @staticmethod
    def get_file_data(file):

        for key, value in file.items():
            binary = value.read()
            value.seek(0)
            return [binary, value]


    @classmethod
    def check_file(cls, binary_file, object_file):

        if object_file.content_type != 'text/plain':
            raise InvalidFileType()

        rows = cls.split_file_to_rows(binary_file)
        for row in rows:
            cls.check_line(row)
             
    
    @classmethod
    def post(cls):
        
        file = request.files
        if len(file) == 0:
            return {'msg': 'You need to upload a file'}, 400
        try:
            binary_file, object_file = cls.get_file_data(file)
            cls.check_file(binary_file, object_file)
            rows = cls.split_file_to_rows(binary_file)
            return TransactionModel.register(rows)

        except (InvalidFileType, InvalidCNABFile) as e:
            return e.msg, e.status
        
        return 'ok'