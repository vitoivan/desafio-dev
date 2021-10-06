from src.controllers.transaction_controller import TransactionController
from os import path

# absolute path of this file


here = path.dirname(__file__)

def get_file(filename):
    return open(path.join(here, f'files/{filename}'), 'rb')


def test_when_transaction_post_is_empty(client):
    
    """If the request was did without an file, then return an error"""

    resp = client.post('/transaction', 
        headers={'Content-Type': 'multipart/form-data'},
        data={}
    )
    assert resp.status_code == 400
    assert resp.json == {'msg': 'You need to upload a file'}


def test_when_the_type_of_file_is_not_txt(client):

    wrong = get_file('incorrect')
    """ If the request was did with a file that is not a .txt,
        then return an error
    """
    resp = client.post('/transaction', 
        headers={'Content-Type': 'multipart/form-data'},
        data={'file': wrong }
    )
    assert resp.status_code == 400
    assert resp.json == {'msg': 'Your file needs to be a .txt'}

def test_when_file_is_not_an_CNAB_file(client):

    """ If the request was did with a file that was not a CNAB file,
        but is a .txt, needs to return an error
    """

    invalid_cnab = get_file('invalid_CNAB.txt')
    resp = client.post('/transaction',
        headers={'Content-Type': 'multipart/form-data'},
        data={'file': invalid_cnab }
    )
    assert resp.status_code == 400
    assert resp.json == {'msg': 'Your file is not a valid CNAB file'}