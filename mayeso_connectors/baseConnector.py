from abc import ABC, abstractmethod

class BaseConnector(ABC):
    '''
    Base connector class
    '''

    def __init__(self):
        pass

    @abstractmethod
    def Execute(self,sql:str):
        '''
        Execute sql statement and return a set of the result
        '''
        pass