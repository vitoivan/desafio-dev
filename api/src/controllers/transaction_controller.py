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
    def check_file(file):
    
        for f, v in file.items():
            uploaded_file = v
            if v.content_type != 'text/plain':
                raise InvalidFileType()

        file = uploaded_file.read()
        uploaded_file.seek(0)
        line = ''
        for letter in file:
            if chr(letter) != '\n':
                line += chr(letter)
            else:
                TransactionController.check_line(line)
                line = ''
    
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