# Mayeso
Mayeso is a package for testing data piplines through comparing their outputs with pre-defined output.

## Architecture
### Tests
In general a Mayeso test (Mtest for short) have two "steps". Each step represent data drawn from a source. the Mtest then stores the results of running the two steps into sets and compare the two sets to see if the data is matching or not.

### Sources
Sources can be anything, form SQL databases to XML files. Mayeso comes with some default connectors with the possibility of extending the `BaseConnector` class to create more connectors.

### Configuration file
A configuration file is needed. It contain the location of the Mtests as well as the definitions of the sources

## How to use:
### configuration file
The configuration file must define all the used sources as well as the Mtests location
```
tests = <location to the tests folder>
source = <source name,type,[other parameters]>
```
currently the sources that are included are `file_delimited` and `oracle`
```
source = <source_name>,oracle,<host/service>,<username>,<password>
source = <source_name>,file_delimited,'<delimiter>'
```
### write tests
Tests follow a simple pattern. Before each step just write the source name as defined in the configuration file between brackets.
```
[source_name1]
step
[source_name2]
step
```
steps nature depends on the source. For DB, they are queries. For files, they are file locations
### run tests
Firstly you create a `ConfigurationManager` object and pass to it the configuration file.
```python
from mayeso import ConfigManager

#Create configuration manager
config = ConfigManager(conf_file)
```
then you register the connectors you need to the `ConfigurationManager`
```python
from mayeso import ConfigManager
from mayeso_connectors import OracleConnector, DelimitedReader

#create configuration manager
config = ConfigManager(conf_file)

#register connectors
config.RegisterConnector("oracle",OracleConnector)
config.RegisterConnector("file_delimited", DelimitedReader)
```
After that you create an object from `MTestExecutor` and pass to it the `ConfigurationManager` object you just created. you use the `MTestExecutor` to run you tests
```python
from mayeso import ConfigManager
from mayeso_connectors import OracleConnector, DelimitedReader

#create configuration manager
config = ConfigManager(conf_file)

#register connectors
config.RegisterConnector("oracle",OracleConnector)
config.RegisterConnector("file_delimited", DelimitedReader)

#create test executor
testExecutor = MTestExecutor(config)

#run tests
testExecutor.RunTests()
```

### Example
please see the `main.py` for how to use the package, `config.txt` for how to write the configuration file and `sampleTests` for how to write tests
## License
This piece of software is released under the [GPL](https://www.gnu.org/licenses/gpl-3.0.en.html) license