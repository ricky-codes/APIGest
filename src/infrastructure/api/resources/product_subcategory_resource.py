import dataclasses
from sys import api_version
from flask_restful import Resource
from flask_restful import reqparse
from flask import request
import datetime

import json

from src.infrastructure.api.services import json_parser

from src.infrastructure.services.product_services import ProductServices
from src.infrastructure.api.errors import service_errors
from src.infrastructure.api.errors import api_errors

class Product_Subcategory_Resource(Resource):
    def __init__(self, **kwargs):

        self.product_services: ProductServices = kwargs["product_services"]

        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument("description", type=str, location="json")
        self.reqparser.add_argument("product_subcategory_parent", type=int, location="json")
        self.reqparser.add_argument("product_category", type=int, location="json")

    def get(self, id):
        try:
            result = self.product_services.get_product_subcategory_by_id(id=id)
        except service_errors.SelectError as err:
            raise api_errors.DbOperationError(err.description)

        return json_parser.dataclass_to_json(result), 202

    def delete(self, id):
        result = self.product_services.delete_product_subcategory_by_id(id)
        if result:
            return "Object deleted successfully", 200
        else:
            return "Error deleting object", 404

    def put(self, id):
        args = self.reqparser.parse_args()
        requested_object = self.product_services.get_product_subcategory_by_id(id=id)
        result = self.product_services.update_product_subcategory(requested_object=requested_object, values_list=args.items())

        return json_parser.dataclass_to_json(result)