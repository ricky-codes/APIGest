# import yaml package
import yaml


# the configuration file to be used
CONFIG_PATH = '././config/development_config.yaml'


def __load_config():
    '''
        This function is responsible for fetching the file, loading the YAML configuration and 
        returning it as a python dictionary

        Parameters:
            None
        Returns:
            configuration (dict): configuration from YAML file as dict
    '''
    try:
        configuration_file = open(CONFIG_PATH)
        configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)
        configuration_file.close()
        return configuration
    except FileNotFoundError:
        print(CONFIG_PATH + " was not found")


def get_connection_config():
    '''
        This function is responsible for loading the config file using __load_config() 
        method and returning only the "CONNECTION" configuration

        Parameters:
            None
        Returns:
            configuration (dict): connection configuration from YAML file
    '''
    configuration = __load_config()
    return configuration['CONNECTION']

def get_mysql_connection_uri():
    configuration = get_connection_config()
    mysql_connection_uri = "mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}?charset=utf8mb4".format(
        configuration['USER'],
        configuration['PASSWORD'],
        configuration['HOST'],
        configuration['PORT'],
        configuration['DATABASE']
    )
    return mysql_connection_uri


def get_logger_config():
    configuration = __load_config()
    return configuration['LOGGER']

def get_flask_config():
    configuration = __load_config()
    return configuration['FLASKAPI']
