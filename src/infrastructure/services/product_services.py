import dataclasses
from datetime import datetime

from src.core.models.product_category_model import ProductCategoryModel
from src.core.models.product_subcategory_model import ProductSubcategoryModel
from src.core.models.product_description_model import ProductDescriptionModel
from src.core.models.product_dimensions_model import ProductDimensionsModel
from src.core.models.product_periodicity_model import ProductPeriodicityModel

from src.infrastructure.services.repository import SqlAlchemyRepository
from src.infrastructure.services.session_wrapper import SessionWrapperAbstract

from src.infrastructure.api.errors import service_errors

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

    def add_product_subcategory(self, description, product_category=None, product_subcategory_parent=None):
        new_product_subcategory = ProductSubcategoryModel(
            description=str(description).upper(),
            created_at=datetime.now()
        )

        new_product_subcategory.product_category = product_category
        if product_subcategory_parent != None:
            new_product_subcategory.product_subcategory_parent = self.get_product_subcategory_by_id(product_subcategory_parent)

        result = self.product_subcategory_repository.insert(new_product_subcategory)

        if result == None:
            raise service_errors.InsertError
        else:
            return result

    def get_all_product_subcategories(self):
        result = self.product_subcategory_repository.get_all()
        if result == None:
            raise service_errors.SelectError
        else:
            return result

    def get_product_subcategory_by_id(self, id):
        result = self.product_subcategory_repository.get_by_id(id)
        if result == None:
            raise service_errors.SelectError
        else:
            return result

    def delete_product_subcategory_by_id(self, id):
        result = self.product_subcategory_repository.delete_by_id(id)
        if result == 0:
            raise service_errors.DeleteError
        else:
            return result

    def update_product_subcategory(self, requested_object, values_list):
        result = self.product_subcategory_repository.update(requested_object=requested_object, values_to_update=values_list)
        if result == None:
            raise service_errors.UpdateError
        else:
            return result
