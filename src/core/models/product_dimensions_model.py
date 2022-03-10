from dataclasses import dataclass
from dataclasses import field

from datetime import date
from enum import Enum

from src.core.interfaces.model_abc import ModelAbstract

class UnityOfMeasure(Enum):
    UNIDADE = 'unidade'
    PACK = 'pack'
    CAIXA = 'caixa'
    MEIA_PALETE = 'meia-palete'
    PALETE = 'palete'

@dataclass
class ProductDimensionsModel(ModelAbstract):
    unity_of_measure: UnityOfMeasure
    unity_per_pack: int
    pack_per_level: int
    level_per_pallet: int
    unity_area: int

