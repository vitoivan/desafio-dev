class InvalidFileType(Exception):

    def __init__(self):
        
        self.msg = {'msg': 'Your file needs to be a .txt'}
        self.status = 400