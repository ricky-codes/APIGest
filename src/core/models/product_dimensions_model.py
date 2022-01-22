from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Product_Dimensions:
    id: int = field(init=False)
    unity_of_sale: str
    quantity_per_pack: Optional[int] = field(init=False)
    pack_by_level: int
    level_by_pallet: int
    unity_area: int