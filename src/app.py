from infrastructure.services.connector import SqlAlchemyConnector
from infrastructure.services.mapper import Mapper
from core.interfaces.connector_abc import Connector

def main(connector):
    connector_base: Connector = connector

    mapper = Mapper().start_mappers()
    session = connector_base.start_connection()
    print(connector_base.get_connection_status())

if __name__ == '__main__':
    main(SqlAlchemyConnector())