from dataclasses import dataclass
from dataclasses import field
from datetime import datetime


@dataclass()
class ModelAbstract:
    id: int = field(init=False)
    modified_at: datetime = field(init=False)
    inserted_at: datetime = field(init=False)
    created_at: datetime = field()