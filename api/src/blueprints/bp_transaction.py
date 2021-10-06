from flask import Blueprint
from src.controllers.transaction_controller import TransactionController

transaction_bp = Blueprint('bp_transation', __name__)

transaction_bp.post('/')(TransactionController.post)