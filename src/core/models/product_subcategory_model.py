from dataclasses import dataclass

from src.core.models import product_category_model
from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductSubcategoryModel(ModelAbstract):
    description: str
    product_category: product_category_model.ProductCategoryModel