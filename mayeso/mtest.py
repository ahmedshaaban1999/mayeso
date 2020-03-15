import re
import threading
from colorama import init,deinit,Fore

class MTest:
    '''
    Represent test file
    '''

    def __init__(self,filepath):
        self.__ReadMTestFile(filepath)
        self.name = filepath.split("\\")[-1].split('.')[0]
        self.connectors = dict()
        self.lock = threading.Lock()

    def __ReadMTestFile(self,filepath: str):
        '''
        Read test file
        '''
        with open(filepath,"r") as file:
            lines = file.readlines()
            s1_line = re.sub(r'[\[\]\n\t ]', '', lines[0])
            c = dict()
            c1_value = ''

            for line in lines[1:]:
                if line.strip()[0] == '[' and line.strip()[-1] == ']':
                    s_line = re.sub(r'[\[\]\n\t ]', '', line)
                    c[s1_line] = c1_value.strip()
                    s1_line = s_line
                    c1_value = ''
                else:
                    c1_value += line
            c[s1_line] = c1_value.strip()
            self.steps = c
        
    def GetMTest(self):
        return self.steps
    
    def AddConnector(self, source: str, connector):
        self.connectors[source] = connector

    def RunTest(self):
        print("Running Test: "+self.name)
        results = list()
        init()
        for k,v in self.steps.items():
            results.append(self.connectors[k].Execute(v))
        if results[0] == results[1]:
            self.lock.acquire()
            print(f'Test {self.name} '+Fore.GREEN+'passed'+Fore.RESET)
            self.lock.release()
        else:
            self.lock.acquire()
            print(f'Test {self.name} '+Fore.RED+'failed'+Fore.RESET)
            self.lock.release()
        deinit()
            
