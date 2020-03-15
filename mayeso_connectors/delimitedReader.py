from mayeso_connectors.baseConnector import BaseConnector

class DelimitedReader(BaseConnector):
    '''
    Reader for delimited files
    '''

    def __init__(self, params: dict):
        self.delimeter = params.get("delimeter")

    def Execute(self, filepath: str):
        '''
        Read a delimited file and return it as a set
        '''
        f2 = set()
        file = open(filepath, "r")
        for line in file.readlines():
            columns = line.strip().split(self.delimeter)
            f2.add(tuple(columns))
        return f2
