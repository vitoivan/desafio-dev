from src.controllers.transaction_controller import TransactionController
from os import path
import pytest
import requests
import json
# absolute path of this file
here = path.dirname(__file__)
host = 'localhost'
port = 3000

url = f'http://{host}:{port}/api/cnab'

def get_file(filename):
    return open(path.join(here, f'files/{filename}'), 'rb')

def get_resp_data(data):
    resp, status = data
    return [json.loads(resp.__dict__['response'][0]), status]
    
def test_when_transaction_post_is_empty(app):
    
    """If the request was did without an file, then return an error"""

    with app.app_context():
        resp, status = get_resp_data(TransactionController.post())
        assert status == 400
        assert resp == {'msg': 'You need to upload a file'}


def test_when_the_type_of_file_is_not_txt(app):

    wrong = get_file('incorrect')
    """ If the request was did with a file that is not a .txt,
        then return an error
    """
    with app.app_context():
        resp, status = get_resp_data(TransactionController.post({'file': wrong}))
        assert status == 400
        assert resp == {'msg': 'Invalid file'}


def test_when_file_is_not_an_CNAB_file(app):

    """ If the request was did with a file that was not a CNAB file,
        but is a .txt, needs to return an error
    """
    invalid_cnab = get_file('invalid_CNAB.txt')
    with app.app_context():
        resp, status = get_resp_data(TransactionController.post({'file': invalid_cnab}))
        assert status == 400
        assert resp == {'msg': 'Your file is not a valid CNAB file'}


def test_check_file_valid_case():

    """ Expect no return and no errors if the file passed match with CNAB pattern"""
    correct = get_file('CNAB.txt')
    file = correct.read().decode()
    
    assert TransactionController.check_file(file) == None


def test_when_send_a_valid_cnab_file(app):

    """ If everything is ok, then insert the files in filesbase and return it """

    correct_cnab = get_file('CNAB.txt')

    with app.app_context():
        resp, status = get_resp_data(TransactionController.post({'file': correct_cnab}))
        assert status == 201


def test_get_file_data():
    
    "Test for the function get file data, this function must return the binary(decoded) of the sended file if is sended a dictionary with the file in the value of that dict"
    correct_cnab = get_file('CNAB.txt')
    received = TransactionController.get_file_data({'Some_text': correct_cnab})
    expected = correct_cnab.read().decode()
    assert expected == received


def test_split_file_to_rows():
    
    "If passed a file (decoded) to this function, it must return an array with each row of that file"
    correct_cnab = get_file('CNAB.txt')
    file_decoded = TransactionController.get_file_data({'Some_text': correct_cnab})

    array_len = len(TransactionController.split_file_to_rows(file_decoded))
    expected = 21
    assert expected == array_len


def test_check_file():

    "If passed a file (decoded) to this function, it must return an array with each row of that file"
    correct_cnab = get_file('CNAB.txt')
    file_decoded = TransactionController.get_file_data({'Some_text': correct_cnab})

    array_len = len(TransactionController.split_file_to_rows(file_decoded))
    expected = 21
    assert expected == array_len


def test_when_send_invalid_query_parameters_on_get(app):
    
    """
        If passed a invalid parameter on query string
        (like NaN, negative numbers or None) then return an error message
    """
    error_msg = {'msg': 'Invalid query parameters'}
    exp_status = 400
    perpage = -1
    pagenumber = 2

    with app.app_context():
        resp, status = get_resp_data(TransactionController.get(perpage, pagenumber))
        assert resp == error_msg
        assert status == exp_status
        perpage = 'Testing'
        pagenumber = 1
        resp, status = get_resp_data(TransactionController.get(perpage, pagenumber))
        assert resp == error_msg
        assert status == exp_status
        resp, status = get_resp_data(TransactionController.get())
        assert resp == error_msg
        assert status == exp_status