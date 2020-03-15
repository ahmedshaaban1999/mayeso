import os

class ConfigManager:
    '''
    Represent Config file
    '''

    def __init__(self,filepath):
        self.__ReadConfigFile(filepath)
        self.connectors = dict()

    def RegisterConnector(self,source:str,connector):
        self.connectors[source] = connector

    def __ReadConfigFile(self,filepath: str):
        '''
        Read Config file and extract sources informations and tests path
        '''
        with open(filepath,"r") as file:
            lines = file.readlines()
            self.sources = dict()
            print("Reading config file")

            for line in lines:
                splits = line.split('=')
                key = splits[0].strip()
                if  key == 'tests':
                    self.tests_path = splits[1].strip()
                elif key == "source": #format of source is SOURCE = NAME,TYPE,...
                    params = splits[1].strip().split(',')
                    s = dict()
                    name = params[0]
                    s["type"] = params[1]

                    if len(params) == 5:
                        # 5 params means it's a db, that makes the format SOURCE = NAME,TYPE,CONNECTION,USERNAME,PASSWORD
                        s["connection"] = params[2]
                        s["username"] = params[3]
                        s["password"] =  params[4]
                    # 
                    if params[1].lower() == "file_delimited": 
                        # format of delimited file source: SOURCE = NAME,TYPE,DELIMETER
                        s["delimeter"] = params[2].strip("'")
                    self.sources[name] = s
                else:
                    print("unknow key in config file: "+key)

    def GetTests(self):
        '''
        Return list of tests paths
        '''
        tests = [os.path.join(self.tests_path, f) for f in os.listdir(
            self.tests_path) if os.path.isfile(os.path.join(self.tests_path, f))]
        return tests

    def CreateConnector(self,source:str):
        '''
        Create connector for the specified source
        '''
        if source not in self.sources:
            print("source not found in config file: "+source)
            return

        source_type = self.sources[source].get("type").lower()
        instance = self.connectors[source_type]
        return instance(self.sources[source])
        
