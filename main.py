import getopt,sys
from mayeso import MTestExecutor, ConfigManager
from mayeso_connectors import OracleConnector, DelimitedReader

def main():
    '''
    An Example on how to use Mayeso
    '''
    argumentList = sys.argv[1:]
    unixOptions = "hc:"
    gnuOptions = ["help", "config="]
    try:
        arguments,values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        sys.exit(2)
    
    conf_file = None
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-c", "--config"):
            conf_file = currentValue
        elif currentArgument in ("-h", "--help"):
            ShowHelp()
            return

    if conf_file is not None:
        #create configuration manager
        config = ConfigManager(conf_file)

        #register connectors
        config.RegisterConnector("oracle",OracleConnector)
        config.RegisterConnector("file_delimited", DelimitedReader)

        #create test executor
        testExecutor = MTestExecutor(config)

        #run tests
        testExecutor.RunTests()

def ShowHelp():
    print("usage: mayeso [arg]\nargs:")
    print("-h,--help:\tshow help menu")
    print("-c,--config config_file:\tprovide configuration file path")

if __name__ == "__main__":
    main()
