from flask import Blueprint
from werkzeug.wrappers import request
from src.controllers.transaction_controller import TransactionController

transaction_bp = Blueprint('bp_transation', __name__, url_prefix='/api/cnab')


@transaction_bp.route('/register', methods=['POST', 'OPTIONS'])
def post():
    
    response, status = TransactionController.post()
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.status = status
    return response


@transaction_bp.get('/')
def get():

    response, status = TransactionController.get()
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.status = status
    return response