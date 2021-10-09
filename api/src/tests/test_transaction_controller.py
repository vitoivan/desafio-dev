from src.controllers.transaction_controller import TransactionController
from src.models.errors import InvalidCNABFile
from os import path
import pytest
import requests
import json

# absolute path of this file

here = path.dirname(__file__)
host = 'localhost'
def get_file(filename):
    return open(path.join(here, f'files/{filename}'), 'rb')


def test_when_transaction_post_is_empty():
    
    """If the request was did without an file, then return an error"""

    resp = requests.post(f'http://{host}:3000/transaction', 
        files={}
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'You need to upload a file'}


def test_when_the_type_of_file_is_not_txt():

    wrong = get_file('incorrect')
    """ If the request was did with a file that is not a .txt,
        then return an error
    """
    resp = requests.post(f'http://{host}:3000/transaction', 
        files={'file': wrong }
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'Invalid file'}

def test_when_file_is_not_an_CNAB_file():

    """ If the request was did with a file that was not a CNAB file,
        but is a .txt, needs to return an error
    """

    invalid_cnab = get_file('invalid_CNAB.txt')
    resp = requests.post(f'http://{host}:3000/transaction',
        files={'file': invalid_cnab }
    )
    assert resp.status_code == 400
    assert json.loads(resp.text) == {'msg': 'Your file is not a valid CNAB file'}


def test_check_line_valid_cases():

    """ Expect no return and no errors if the string passed match with CNAB pattern"""

    line1 = '3201903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       '
    line2 = '5201903010000013200556418150633123****7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'
    line3 = '3201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA'
    line4 = '2201903010000011200096206760173648****0099234234JOÃO MACEDO   BAR DO JOÃO       '
    line5 = '1201903010000015200096206760171234****7890233000JOÃO MACEDO   BAR DO JOÃO       '
    line6 = '2201903010000010700845152540738723****9987123333MARCOS PEREIRAMERCADO DA AVENIDA'
    line7 = '2201903010000050200845152540738473****1231231233MARCOS PEREIRAMERCADO DA AVENIDA'
    line8 = '3201903010000060200232702980566777****1313172712JOSÉ COfSTA    MERCEARIA 3 IRMÃOS'
    line9 = '1201903010000020000556418150631234****3324090002MARIA JOSEFINALOJA DO Ó - MATRIZ'
    line10 = '5201903010000080200845152540733123****7687145607MARCOS PEREIRAMERCADO DA AVENIDA'

    assert TransactionController.check_line(line1) == None
    assert TransactionController.check_line(line2) == None
    assert TransactionController.check_line(line3) == None
    assert TransactionController.check_line(line4) == None
    assert TransactionController.check_line(line5) == None
    assert TransactionController.check_line(line6) == None
    assert TransactionController.check_line(line7) == None
    assert TransactionController.check_line(line8) == None
    assert TransactionController.check_line(line9) == None
    assert TransactionController.check_line(line10) == None


def test_check_line_invalid_cases():

    """ Expect an error if the line does not match with the CNAB pattern """

    line1 = '301903010000014200096206760174753****3153153453JOÃO MACEDO   BAR DO JOÃO       '
    line2 = '5201903010000013200556418150633123***7687145607MARIA JOSEFINALOJA DO Ó - MATRIZ'
    line3 = '3201903010000012200845152540736777****1313172712MARCOS PEREIRAMERCAD DA AVENIDA'
    line4 = '2201903010000011200096206760173648****0099234234JOÃO MACEDO   BA DO JOÃO       '
    line5 = '1201903010000015200096206760171234****7890233000JOÃO MACEDO   BAR DO JOÃO       '
    line6 = '2201903010000010700845152540738723****998723333MARCOS PEREIRAMERCADO DA AVENIDA'
    line7 = '2201903010000050200845152540738473****131231233MARCOS PEREIRAMERCADO DA AVENIDA'
    line8 = '3201903010000060200232702980566777****1313172712JOSÉ COfSTA    MERCEARIA 3 IRMÃOS'
    line9 = '120190301000002000055641815034****324090002MARIA JOSEFINALOJA DO Ó - MATRIZ'
    line10 = '52019030100000802008451525a40733123****7687145607MARCOS PEREIRAMERCADO DA AVENIDA'

    with pytest.raises(InvalidCNABFile):
        TransactionController.check_line(line1)
        TransactionController.check_line(line2)
        TransactionController.check_line(line3)
        TransactionController.check_line(line4)
        TransactionController.check_line(line5)
        TransactionController.check_line(line6)
        TransactionController.check_line(line7) 
        TransactionController.check_line(line8)
        TransactionController.check_line(line9)
        TransactionController.check_line(line10)


def test_when_send_a_valid_cnab_file():

    """ If everything is ok, then insert the files in filesbase and return it """

    correct_cnab = get_file('CNAB.txt')

    resp = requests.post(f'http://{host}:3000/transaction',
        files={'file': correct_cnab }
    )

    assert resp.status_code == 201