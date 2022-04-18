from dataclasses import dataclass
from dataclasses import field
from typing import List
from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductCategoryModel(ModelAbstract):
    description: str 
    iva: int