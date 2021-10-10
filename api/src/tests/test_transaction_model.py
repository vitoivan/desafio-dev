from src.models.transaction_model import TransactionModel
from datetime import datetime

def test_normalize_row():

    """
        Given an row of a CNAB file, this function must return
        an dictionary with the data
    """
    row = '5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'

    expected = {
        'type': 'Recebimento Empréstimo',
        'date': datetime.date(datetime.strptime('20190301', '%Y%m%d')),
        'value': 132.0,
        'cpf': '55641815063',
        'card': '3123****7687',
        'time': datetime.time(datetime.strptime('145607', '%H%M%S')),
        'owner_name': 'MARIA JOSEFINA',
        'shop_name': 'LOJA DO Ó - MATRIZ'
    }
    assert TransactionModel.normalize_row(row) == expected


def test_get_transactions():

    """
        Checking the quantity of items returned of get_transactions
        function (must be more than 10 items on database)
    """
    resp = TransactionModel.get_transactions(1, 1)
    assert 1 == len(resp)

    resp = TransactionModel.get_transactions(5, 2)
    assert 5 == len(resp)

    resp = TransactionModel.get_transactions(8, 1)
    assert 8 == len(resp)