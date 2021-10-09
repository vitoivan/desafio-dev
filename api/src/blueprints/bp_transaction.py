from flask import Blueprint
from werkzeug.wrappers import request
from src.controllers.transaction_controller import TransactionController

transaction_bp = Blueprint('bp_transation', __name__)


@transaction_bp.route('/transaction', methods=['POST', 'OPTIONS'])
def post():
    
    response, status = TransactionController.post()
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.status = status
    return response


@transaction_bp.get('/transaction')
def get():

    response, status = TransactionController.get()
    response.headers.add("Access-Control-Allow-Headers", "*")
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.status = status
    return response