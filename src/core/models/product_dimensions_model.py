from dataclasses import dataclass
from dataclasses import field

from datetime import date

@dataclass
class ProductDimensionsModel():
    id: int = field(init=False, repr=False)
    unity_of_measure: str
    unity_per_pack: int
    pack_per_level: int
    level_per_pallet: int
    unity_area: int