import yaml

CONFIG_PATH = '././config/development_config.yaml'

def __load_config():
    try:
        configuration_file = open(CONFIG_PATH)
        configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)
        return configuration
    except FileNotFoundError:
        print(CONFIG_PATH + " was not found")


def get_connection_config():
    configuration = __load_config()
    return configuration['CONNECTION']