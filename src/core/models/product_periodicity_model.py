from dataclasses import dataclass
from dataclasses import field

from datetime import date

@dataclass
class ProductPeriodicityModel():
    id: int = field(init=False, repr=False)
    entry_on_warehouse: date = field(default_factory=date)
    expire_date: date = field(default_factory=date)