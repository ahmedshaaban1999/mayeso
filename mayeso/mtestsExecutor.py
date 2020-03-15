import threading
from mayeso import ConfigManager, MTest

class MTestExecutor:
    '''
    Create configuration manager and tests for all the test
    '''

    def __init__(self, config: ConfigManager):
        self.mtests = list()
        for t in config.GetTests():
            mtest = MTest(t)
            for s in mtest.GetMTest().keys():
                mtest.AddConnector(s, config.CreateConnector(s))
            self.mtests.append(mtest)

    def RunTests(self):
        '''
        Run all the tests
        '''
        processes = list()
        for test in self.mtests:
            p = threading.Thread(target=test.RunTest)
            p.start()
            processes.append(p)
        for p in processes:
            p.join()
