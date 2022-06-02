from flask import Flask
from flask_restful import Api
#----------------------------
from src.shared import parse_config
from src.infrastructure.api.blueprints.admin_blueprint import main_blueprint
from src.infrastructure.api.blueprints.errors_blueprint import errors
from src.infrastructure.api.resources.main_home_resource import Main_Home
from src.infrastructure.api.resources.product_subcategory_resource import Product_Subcategory_Resource
from src.infrastructure.api.resources.product_subcategories_resource import Product_Subcategories_Resource

from src.infrastructure.services.product_services import ProductServices
from src.infrastructure.services.session_wrapper import SqlSession


configuration = parse_config.get_flask_config()

product_services = ProductServices(session = SqlSession())

app = Flask(__name__)
api = Api(main_blueprint)
api.add_resource(Main_Home, "/")
api.add_resource(Product_Subcategory_Resource, "/product_subcategories/<id>", resource_class_kwargs={"product_services": product_services})
api.add_resource(Product_Subcategories_Resource, "/product_subcategories", resource_class_kwargs={"product_services": product_services})

app.config["FLASK_ENV"] = configuration['DEVELOPMENT']['ENVIRONMENT']
app.config["SECRET_KEY"] = configuration['DEVELOPMENT']['SECRET_KEY']
app.config["DEBUG"] = configuration['DEVELOPMENT']['DEBUG']

app.register_blueprint(errors)
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(port=configuration['DEVELOPMENT']['FLASK_RUN_PORT'])