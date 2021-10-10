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


def test_when_transaction_post_is_empty():
    
    """If the request was did without an file, then return an error"""

    resp = requests.post(f'{url}/register', 
        files={}
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'You need to upload a file'}


def test_when_the_type_of_file_is_not_txt():

    wrong = get_file('incorrect')
    """ If the request was did with a file that is not a .txt,
        then return an error
    """
    resp = requests.post(f'{url}/register', 
        files={'file': wrong }
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'Invalid file'}


def test_when_file_is_not_an_CNAB_file():

    """ If the request was did with a file that was not a CNAB file,
        but is a .txt, needs to return an error
    """

    invalid_cnab = get_file('invalid_CNAB.txt')
    resp = requests.post(f'{url}/register',
        files={'file': invalid_cnab }
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'Your file is not a valid CNAB file'}


def test_check_file_valid_case():

    """ Expect no return and no errors if the file passed match with CNAB pattern"""
    correct = get_file('CNAB.txt')
    file = correct.read().decode()
    
    assert TransactionController.check_file(file) == None


def test_when_send_a_valid_cnab_file():

    """ If everything is ok, then insert the files in filesbase and return it """

    correct_cnab = get_file('CNAB.txt')

    resp = requests.post(f'{url}/register',
        files={'file': correct_cnab }
    )

    assert resp.status_code == 201


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