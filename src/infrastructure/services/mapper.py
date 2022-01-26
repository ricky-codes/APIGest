from sqlalchemy.orm import registry, relationship

from src.core.models import product_description_model, product_dimensions_model, product_periodicity_model
from src.infrastructure.data import product_periodicity, product_dimensions, product_description, metadata


class Mapper():

    def __init__(self) -> None:
        self.__metadata_obj = metadata.Metadata().get_metadata()
        self.__mapper_registry = registry(metadata= self.__metadata_obj)

    def start_mappers(self):
        self.__mapper_registry.map_imperatively(product_periodicity_model.Product_Periodicity, product_periodicity.product_periodicity_table)
        self.__mapper_registry.map_imperatively(product_dimensions_model.Product_Dimensions, product_dimensions.product_dimensions_table)
        self.__mapper_registry.map_imperatively(product_description_model.Product_Description, 
                                        product_description.product_description_table, 
                                        properties={
                                            'product_dimensions': relationship(product_dimensions_model.Product_Dimensions,
                                                                                backref='product_dimensions_table'),
                                            'product_periodicity': relationship(product_periodicity_model.Product_Periodicity,
                                                                                backref='product_periodicity_table')
                                        })