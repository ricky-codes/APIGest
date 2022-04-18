from dataclasses import dataclass, field

from src.core.interfaces.model_abc import ModelAbstract

from src.core.models import product_dimensions_model
from src.core.models import product_periodicity_model
from src.core.models import product_category_model
from src.core.models import product_subcategory_model

@dataclass
class ProductDescriptionModel(ModelAbstract):
    name: str
    product_subcategory: product_subcategory_model.ProductSubcategoryModel
    internal_code: int
    ean: int
    product_dimensions: product_dimensions_model.ProductDimensionsModel
    product_periodicity: product_periodicity_model.ProductPeriodicityModel

