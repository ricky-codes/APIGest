from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref
from sqlalchemy.orm import registry

from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel
from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel

from src.infrastructure.orm.product_periodicity_entity import product_periodicity_table
from src.infrastructure.orm.product_dimensions_entity import product_dimensions_table
from src.infrastructure.orm.product_description_entity import product_description_table
from src.infrastructure.orm.product_category_entity import product_category_table
from src.infrastructure.orm.product_subcategory_entity import product_subcategory_table

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

        registry().map_imperatively(ProductPeriodicityModel, product_periodicity_table)
        registry().map_imperatively(ProductDimensionsModel, product_dimensions_table)
        registry().map_imperatively(ProductDescriptionModel, product_description_table, properties={
            'product_dimensions': relationship(ProductDimensionsModel), 
            'product_periodicity': relationship(ProductPeriodicityModel),
            'product_subcategory': relationship(ProductSubcategoryModel)
        })
        registry().map_imperatively(ProductCategoryModel, product_category_table, properties={
            'product_subcategories': relationship(ProductSubcategoryModel, backref='product_category')
        })
        registry().map_imperatively(ProductSubcategoryModel, product_subcategory_table, properties={
            'product_subcategory_parent': relationship(ProductSubcategoryModel)
        })