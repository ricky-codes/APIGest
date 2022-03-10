from dataclasses import dataclass
from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductCategoryModel(ModelAbstract):
    description: str
    iva: int