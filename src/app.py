from datetime import date
from core.models.product_description_model import ProductDescriptionModel

from infrastructure.services.connector import SqlAlchemyConnector
from infrastructure.services.mapper import Mapper

from core.interfaces.connector_abc import Connector

from sqlalchemy.orm import mapper

from sqlalchemy.orm.session import Session

from core.models.product_dimensions_model import ProductDimensionsModel
from core.models.product_periodicity_model import ProductPeriodicityModel

from infrastructure.data.product_periodicity_entity import product_periodicity_table
from infrastructure.data.product_dimensions_entity import product_dimensions_table

def main(connector):
    connector_base: Connector = connector
    session: Session = connector_base.start_connection()

    new_product_periodicity = ProductPeriodicityModel(entry_on_warehouse=date(day=12,month=11,year=2022), expire_date=date(day=23,month=10,year=1999))
    new_product_dimensions = ProductDimensionsModel(
        unity_of_measure='unidade',
        unity_per_pack=12,
        pack_per_level=54,
        level_per_pallet=5,
        unity_area=76
    )

    new_product_description = ProductDescriptionModel(
        name='Compal Frutos Vermelhos',
        category='Sumos',
        subcategory='Nectares',
        internal_code='12345',
        ean='53245676543245',
        product_dimensions=new_product_dimensions,
        product_periodicity=new_product_periodicity
    )

    print(new_product_periodicity)
    print(new_product_dimensions)
    print('\n-----------------------\n')
    print(new_product_description)

if __name__ == '__main__':
    Mapper().start_mappers()
    main(SqlAlchemyConnector())