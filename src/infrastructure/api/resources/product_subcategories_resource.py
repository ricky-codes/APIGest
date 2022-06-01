import dataclasses
from flask_restful import Resource
from flask_restful import reqparse
from flask import request
import datetime
import json
import marshal

from src.infrastructure.api.services import json_parser

from src.infrastructure.services.product_services import ProductServices


class Product_Subcategories_Resource(Resource):
    def __init__(self, **kwargs):

        self.product_services: ProductServices = kwargs["product_services"]

        self.parser = reqparse.RequestParser()
        self.parser.add_argument("description", type=str, location="json", required=True)
        self.parser.add_argument("product_subcategory_parent", type=int, location="json")
        self.parser.add_argument("product_category", type=int, location="json")


    def get(self):
        result = self.product_services.get_all_product_subcategories()
        if result == None:
            return "No objects in the database", 404

        parsed_result = json_parser.dataclass_list_to_json(result)
        return parsed_result, 202


    def post(self):

        args = self.parser.parse_args()

        result = self.product_services.add_product_subcategory(description=args["description"], product_subcategory_parent=args["product_subcategory_parent"])

        if result == None:
            return "Error inserting in database", 403

        parsed_result = json_parser.validation_to_json(success=True, message=str(result))
        return parsed_result 
