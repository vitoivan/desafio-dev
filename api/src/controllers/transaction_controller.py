from flask import request, jsonify, current_app
from src.models.errors import InvalidFileType, InvalidCNABFile
import re

class TransactionController:

    @staticmethod
    def check_line(row: str):
        reg = r"(\d{34})(\*{4})(\d{10})(.{32,34})"
        if re.fullmatch(reg, row) == None:
            raise InvalidCNABFile()
    
    @staticmethod
    def split_file(file):
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
    def check_file(cls, file):
     
        binary_file, object_file = cls.get_file_data(file)

        if object_file.content_type != 'text/plain':
            raise InvalidFileType()

        rows = TransactionController.split_file(binary_file)
        for row in rows:
            TransactionController.check_line(row)
             
    
    @staticmethod
    def post():
        
        file = request.files
        if len(file) == 0:
            return {'msg': 'You need to upload a file'}, 400
        try:
            TransactionController.check_file(file)
        except (InvalidFileType, InvalidCNABFile) as e:
            return e.msg, e.status
        
        return 'ok'