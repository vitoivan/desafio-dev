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

    @staticmethod
    def post():
        
        file = request.files
        if len(file) == 0:
            return {'msg': 'You need to upload a file'}, 400
        try:
            TransactionController.check_file(file)
        except InvalidFileType as e:
            return e.msg, e.status
        
    
        return 'ok'