from infrastructure.services import connector
from core.interfaces.connector_abc import Connector

def main(connector):
    connector_base: Connector = connector

    session = connector_base.start_connection()
    print(connector_base.get_connection_status())

if __name__ == '__main__':
    main(connector.SqlAlchemyConnector())