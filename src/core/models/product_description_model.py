from dataclasses import dataclass
from dataclasses import field

from datetime import date

from src.core.interfaces.model_abc import ModelAbstract

from src.core.models import product_dimensions_model
from src.core.models import product_periodicity_model

@dataclass
class ProductDescriptionModel(ModelAbstract):
    name: str
    category: str
    subcategory: str
    internal_code: int
    ean: int
    product_dimensions: product_dimensions_model.ProductDimensionsModel
    product_periodicity: product_periodicity_model.ProductPeriodicityModel