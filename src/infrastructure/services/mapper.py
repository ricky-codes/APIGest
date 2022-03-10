from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel
from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel

from src.infrastructure.data.product_periodicity_entity import product_periodicity_table
from src.infrastructure.data.product_dimensions_entity import product_dimensions_table
from src.infrastructure.data.product_description_entity import product_description_table
from src.infrastructure.data.product_category_entity import product_category_table
from src.infrastructure.data.product_subcategory_entity import product_subcategory_table

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
            'product_dimensions': relationship(ProductDimensionsModel, cascade='all, delete-orphan', single_parent=True), 
            'product_periodicity': relationship(ProductPeriodicityModel, cascade='all, delete-orphan', single_parent=True),
            'product_category': relationship(ProductCategoryModel, cascade='all, delete-orphan', single_parent=True),
            'product_subcategory': relationship(ProductSubcategoryModel, cascade='all, delete-orphan', single_parent=True)
        })
        mapper(ProductCategoryModel, product_category_table)
        mapper(ProductSubcategoryModel, product_subcategory_table, properties={
            'product_category': relationship(ProductCategoryModel, cascade='all, delete-orphan', single_parent=True)
        })