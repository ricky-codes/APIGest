import dataclasses
from datetime import datetime

from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel
from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel

from src.infrastructure.services.repository import SqlAlchemyRepository
from src.infrastructure.services.session_wrapper import SessionWrapperAbstract

class ProductServices():

    def __init__(self, session):
        self.session_wrapper: SessionWrapperAbstract = session

        self.session_factory = self.session_wrapper.get_session()
        self.session = self.session_factory()

        self.product_category_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=self.session, object_type=ProductCategoryModel)
        self.product_subcategory_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=self.session, object_type=ProductSubcategoryModel)
        self.product_description_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=self.session, object_type=ProductDescriptionModel)
        self.product_dimensions_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=self.session, object_type=ProductDimensionsModel)
        self.product_periodicity_repository: SqlAlchemyRepository = SqlAlchemyRepository(session=self.session, object_type=ProductPeriodicityModel)

    def add_product_description(self, name, internal_code, ean, product_subcategory, product_dimensions, product_periodicity):
        new_product_description = ProductDescriptionModel(
            name=name,
            internal_code=internal_code,
            ean=ean,
            product_subcategory=product_subcategory,
            product_dimensions=product_dimensions,
            product_periodicity=product_periodicity,
            created_at=datetime.now()
        )

        try:
            self.product_description_repository.insert(new_product_description)
            self.session.commit()
        except:
            return "Error while insert"

    def get_product_subcategory_by_name(self, description):
        result = self.product_subcategory_repository.get_by_filter(ProductSubcategoryModel.description == description)
        return result

    def get_all_product_subcategories(self):
        result = self.product_subcategory_repository.get_by_filter(ProductSubcategoryModel.id > 0)
        return result

    def get_product_subcategory_by_id(self, id):
        result = self.product_subcategory_repository.get_by_id(id)
        return result
