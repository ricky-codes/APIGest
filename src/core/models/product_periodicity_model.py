from dataclasses import dataclass
from dataclasses import field

from datetime import date

from src.core.interfaces.model_abc import ModelAbstract

@dataclass
class ProductPeriodicityModel(ModelAbstract):
    entry_on_warehouse: date = field(default_factory=date)
    expire_date: date = field(default_factory=date)