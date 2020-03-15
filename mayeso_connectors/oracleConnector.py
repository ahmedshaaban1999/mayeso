from mayeso_connectors.baseConnector import BaseConnector
import cx_Oracle

class OracleConnector(BaseConnector):
    '''
    Connector for oracle DB
    '''

    def __init__(self,params: dict):

        self.conn = cx_Oracle.Connection(params.get("username"), params.get(
            "password"), params.get("connection"))
        self.cur = self.conn.cursor()

    def Execute(self,sql: str):
        '''
        Execute sql statement and return a set of the result
        '''
        self.cur.execute(sql)
        f1 = set()
        while True:
            rows = self.cur.fetchmany()
            if not rows:
                break
            for row in rows:
                str_row = []
                for column in row:
                    str_row.append(str(column))
                f1.add(tuple(str_row))
        return f1
