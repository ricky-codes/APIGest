from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
import mysql.connector.errors

from models.base import Base
import parse_config


def start_connection():
    connection = parse_config.connection_config()
    try:
        engine = create_engine(f"mysql+mysqlconnector://{connection['USER']}:{connection['PASSWORD']}@{connection['HOST']}?charset=utf8mb4")
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        return session
    except mysql.connector.DatabaseError:
        print("Cannot connect to the database")
    except KeyError as err:
        print("The following keys aren't correct: " + str(err.args))


if __name__ == "__main__":
    start_connection()