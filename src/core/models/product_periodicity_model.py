from dataclasses import dataclass
from dataclasses import field

from datetime import datetime

@dataclass
class ProductPeriodicityModel():
    id: int = field(init=False)
    entry_on_warehouse: datetime = field(default_factory=datetime)
    expire_date: datetime = field(default_factory=datetime)