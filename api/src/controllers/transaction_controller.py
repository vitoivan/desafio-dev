from flask import request, jsonify, current_app
from werkzeug.utils import validate_arguments

class TransactionController:

    @staticmethod
    def post(file = None):
        
        if file == None:
            file = request.files
        for f, v in file.items():
            if v.content_type != 'text/plain':
                return {'msg': 'Your file needs to be a .txt'}, 400
        return {'msg': 'You need to upload a file'}, 400