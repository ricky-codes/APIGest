import dataclasses
from sys import api_version
from flask_restful import Resource
from flask_restful import reqparse
from flask import request
import datetime
import logging
import logging.config
import json

from src.infrastructure.api.services import json_parser

from src.shared import parse_config

from src.infrastructure.services.product_services import ProductServices
from src.infrastructure.api.errors import service_errors
from src.infrastructure.api.errors import api_errors

class Product_Subcategory_Resource(Resource):
    def __init__(self, **kwargs):

        logging.config.dictConfig(parse_config.get_logger_config())
        self.logger = logging.getLogger("dev")

        self.product_services: ProductServices = kwargs["product_services"]

        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument("description", type=str, location="json")
        self.reqparser.add_argument("product_subcategory_parent", type=int, location="json")
        self.reqparser.add_argument("product_category", type=int, location="json")

    def get(self, id):
        try:
            result = self.product_services.get_product_subcategory_by_id(id=id)
            return json_parser.dataclass_to_json(result), 202
        except service_errors.SelectError as err:
            self.logger.error("Error in get_product_subcategory_by_id.")
            raise api_errors.DbOperationError(err.description)

    def delete(self, id):
        try:
            result = self.product_services.delete_product_subcategory_by_id(id)
            return "Object deleted successfully", 200
        except service_errors.DeleteError as err:
            self.logger.error("Error in delete_product_subcategory_by_id")
            raise api_errors.DbOperationError(err.description)

    def put(self, id):
        args = self.reqparser.parse_args()
        try:
            requested_object = self.product_services.get_product_subcategory_by_id(id=id)
            result = self.product_services.update_product_subcategory(requested_object=requested_object, values_list=args.items())
            return json_parser.dataclass_to_json(result)
        except service_errors.UpdateError as err:
            self.logger.error("Error in update_product_subcategory")
            raise api_errors.DbOperationError(err.description)