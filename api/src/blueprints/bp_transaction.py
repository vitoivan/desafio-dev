from flask import Blueprint
from src.controllers.transaction_controller import TransactionController

bp_transation = Blueprint('bp_transation', __name__)

bp_transation.post('/')(TransactionController.post)