from datetime import datetime

from infrastructure.services.connector import SqlAlchemyConnector
from core.interfaces.connector_abc import Connector

from sqlalchemy.orm import mapper

from sqlalchemy.orm.session import Session

from core.models.product_periodicity_model import ProductPeriodicityModel
from infrastructure.data.product_periodicity_entity import product_periodicity_table

def main(connector):
    connector_base: Connector = connector
    session: Session = connector_base.start_connection()

    print(mapper(ProductPeriodicityModel, product_periodicity_table))

    session.add(ProductPeriodicityModel(entry_on_warehouse=datetime(day=12,month=11,year=2022), expire_date=datetime(day=23,month=10,year=1999)))
    session.commit()

    print(connector_base.get_connection_status())

if __name__ == '__main__':
    main(SqlAlchemyConnector())