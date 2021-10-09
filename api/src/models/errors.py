class InvalidCNABFile(Exception):

    def __init__(self):
        
        self.msg = {'msg': 'Your file is not a valid CNAB file'}
        self.status = 400