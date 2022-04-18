from dataclasses import dataclass, field

from src.core.models.product_category_model import ProductCategoryModel
from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductSubcategoryModel(ModelAbstract):
    description: str
    product_category: ProductCategoryModel = field(init=False)
    product_subcategory_parent: 'ProductSubcategoryModel' = field(init=False)