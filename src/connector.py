from sqlite3 import DatabaseError
import mysql.connector
import yaml

CONFIG_PATH = './config/development_config.yaml'

with open(CONFIG_PATH) as configuration_file:
    configuration = yaml.load(configuration_file, Loader=yaml.FullLoader)
    database_config = configuration['DATABASE']

try:
    db = mysql.connector.connect(
        host=database_config['HOST'],
        username=database_config['USER'],
        password=database_config['PASSWORD'],
        port= database_config['PORT']
    )
except mysql.connector.errors.DatabaseError:
    print("Connection error")
