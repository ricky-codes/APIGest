from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Product_Periodicity:
    id: int = field(init= False)
    entry_on_warehouse: datetime = None
    expire_date: str = None

