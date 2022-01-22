from sqlalchemy import create_engine, engine, orm
import mysql.connector.errors

from infrastructure.mapper import start_mappers
from infrastructure.data import product_description
from core import parse_config



def start_connection():
    connection = parse_config.get_connection_config()
    try:
        engine = create_engine(f"mysql+mysqlconnector://{connection['USER']}:{connection['PASSWORD']}@{connection['HOST']}?charset=utf8mb4")
        Session = orm.sessionmaker(bind=engine)
        session = Session()
        return session
    except mysql.connector.DatabaseError:
        print("Cannot connect to the database")
    except KeyError as err:
        print("The following keys aren't correct: " + str(err.args))