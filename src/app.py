from datetime import date

from sqlalchemy.orm import mapper


# imports from core
from core.models.product_dimensions_model import ProductDimensionsModel
from core.models.product_periodicity_model import ProductPeriodicityModel
from core.models.product_description_model import ProductDescriptionModel

from core.interfaces.connection_abc import ConnectionAbstract
from core.interfaces.model_abc import ModelAbstract
from core.interfaces.unit_of_work_abc import UnitOfWorkAbstract

# imports from infrastructure
from infrastructure.services.connection import SqlAlchemyConnection
from infrastructure.services.unit_of_work import SqlAlchemyUnitOfWork
from infrastructure.services.mapper import Mapper

from infrastructure.data.product_periodicity_entity import product_periodicity_table
from infrastructure.data.product_dimensions_entity import product_dimensions_table


def main(connector, unitofwork):
    '''
        This function is responsible to initialize everything at startup that needs to be initialized

        Parameters:
            connector (Connector): Connector instance that will be used
        Returns:
            None
    '''
    connector_base: ConnectionAbstract = connector
    unitofwork_base: UnitOfWorkAbstract = unitofwork

    connection = connector_base.start_connection()
    session = unitofwork_base.enter()

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

    base_product: ModelAbstract = new_product_description 

    print(new_product_periodicity)
    print(new_product_dimensions)
    print('\n-----------------------\n')
    print(base_product)

    session.add(new_product_description)
    session.commit()

if __name__ == '__main__':
    # Instanciate the mappers and pass the Connector used to the main function
    Mapper().start_mappers()
    current_connection = SqlAlchemyConnection()
    current_unit_of_work = SqlAlchemyUnitOfWork(current_connection)
    main(current_connection, current_unit_of_work)
