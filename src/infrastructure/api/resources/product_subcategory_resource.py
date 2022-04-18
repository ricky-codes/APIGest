from flask_restful import Resource
from flask import request

from src.infrastructure.api.services import json_parser

from src.core.interfaces.model_abc import ModelAbstract

from src.infrastructure.services.session_wrapper import SqlSession
from src.infrastructure.services.product_services import ProductServices

class Product_Subcategory_Resource(Resource):
    def __init__(self, **kwargs):
        self.product_services: ProductServices = kwargs["product_services"]

    def get(self):
        data = request.args
        if 'id' in data:
            result = self.product_services.get_product_subcategory_by_id(data['id'])
        else:
            result = self.product_services.get_all_product_subcategories()

        if result == None:
            return json_parser.validation_to_json(success=False, message='No data was found'), 404

        parsed_result = json_parser.dataclass_to_json(result)
        return json_parser.validation_to_json(success=True, message=parsed_result), 200
