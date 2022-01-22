from infrastructure.data import product_periodicity, product_dimensions, product_description
from sqlalchemy.orm import registry, relationship
from sqlalchemy import MetaData, inspect
from core.models import product_description_model, product_dimensions_model, product_periodicity_model


metadata = MetaData()
mapper_registry = registry(metadata= metadata)


def start_mappers():
    mapper_registry.map_imperatively(product_periodicity_model.Product_Periodicity, product_periodicity.product_periodicity_table)
    mapper_registry.map_imperatively(product_dimensions_model.Product_Dimensions, product_dimensions.product_dimensions_table)
    mapper_registry.map_imperatively(product_description_model.Product_Description, 
                                    product_description.product_description_table, 
                                    properties={
                                        'product_dimensions': relationship(product_dimensions_model.Product_Dimensions,
                                                                            backref='product_dimensions_table'),
                                        'product_periodicity': relationship(product_periodicity_model.Product_Periodicity,
                                                                            backref='product_periodicity_table')
                                    })

    mapped = inspect(product_periodicity_model.Product_Periodicity)
    print(mapped.all_orm_descriptors.keys())