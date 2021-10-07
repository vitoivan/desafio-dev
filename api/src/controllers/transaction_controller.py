from flask import request, jsonify, current_app
from src.models.errors import InvalidFileType
import re

class TransactionController:

    @staticmethod
    def check_file(file):
        reg = "(\d{34})(\*\*\*\*)(\d{10})(.{32})"

        for f, v in file.items():
            if v.content_type != 'text/plain':
                raise InvalidFileType()
                return {'msg': 'Your file needs to be a .txt'}, 400

    @staticmethod
    def post(file = None):
        
        if file == None:
            file = request.files
        try:
            TransactionController.check_file(file)
        except InvalidFileType as e:
            return e.msg, e.status
        
    
        return {'msg': 'You need to upload a file'}, 400