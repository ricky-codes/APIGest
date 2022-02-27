from dataclasses import dataclass
from dataclasses import field

from datetime import date

from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductDimensionsModel(ModelAbstract):
    unity_of_measure: str
    unity_per_pack: int
    pack_per_level: int
    level_per_pallet: int
    unity_area: int