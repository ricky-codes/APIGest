import dataclasses
from flask_restful import Resource
from flask_restful import reqparse
from flask import request
import datetime
import logging
import logging.config

from src.infrastructure.api.services import json_parser

from src.shared import parse_config

from src.infrastructure.services.product_services import ProductServices

from src.infrastructure.api.errors import service_errors
from src.infrastructure.api.errors import api_errors


class Product_Subcategories_Resource(Resource):
    def __init__(self, **kwargs):

        self.product_services: ProductServices = kwargs["product_services"]

        logging.config.dictConfig(parse_config.get_logger_config())
        self.logger = logging.getLogger("dev")

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("description", type=str, location="json", required=True)
        self.parser.add_argument("product_subcategory_parent", type=int, location="json")
        self.parser.add_argument("product_category", type=int, location="json")


    def get(self):
        try:
            result = self.product_services.get_all_product_subcategories()
            parsed_result = json_parser.dataclass_list_to_json(result)
            return parsed_result, 202
        except service_errors.SelectError as err:
            self.logger.error("Error in get_all_product_subcategories")
            raise api_errors.DbOperationError(err.description)


    def post(self):

        args = self.parser.parse_args()

        try:
            result = self.product_services.add_product_subcategory(description=args["description"], product_subcategory_parent=args["product_subcategory_parent"])
            parsed_result = json_parser.validation_to_json(success=True, message=str(result))
            return parsed_result 
        except service_errors.InsertError as err:
            self.logger.error("Error in add_product_subcategory")
            raise api_errors.DbOperationError(err.description)

