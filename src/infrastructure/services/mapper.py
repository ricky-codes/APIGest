from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship

from core.models.product_description_model import ProductDescriptionModel
from core.models.product_dimensions_model import ProductDimensionsModel
from core.models.product_periodicity_model import ProductPeriodicityModel

from infrastructure.data.product_periodicity_entity import product_periodicity_table
from infrastructure.data.product_dimensions_entity import product_dimensions_table
from infrastructure.data.product_description_entity import product_description_table

class Mapper():
    '''
        This class holds all the data and methods related to the mapping process
        used by sqlalchemy.orm.mapper

        Methods:
            start_mappers()
    '''

    def start_mappers(self) -> None:
        '''
            This method is responsible to initialize all mappers, mapping models (dataclasses) 
            and entities (sqlalchemy.Table) along with their relationships

            Parameters:
                None
            Returns:
                None
        '''
        mapper(ProductPeriodicityModel, product_periodicity_table)
        mapper(ProductDimensionsModel, product_dimensions_table)
        mapper(ProductDescriptionModel, product_description_table, properties={
            'product_dimensions': relationship(ProductDimensionsModel, backref='product_dimensions_id'), 
            'product_periodicity': relationship(ProductPeriodicityModel, backref='product_periodicity_id'),
        })