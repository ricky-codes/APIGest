from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from datetime import date
import uuid


@dataclass()
class ModelAbstract:
    '''This class defines a base class for every model
    
    Attributes:
        id - id for database
        modified_at - saves the current date when modifying an object
        inserted_at - saves the current date when inserting an object
        created_at - saves the current date when creating an object
    '''
    id: int = field(init=False, default=uuid.uuid4())
    modified_at: datetime = field(init=False, default=datetime.now())
    created_at: datetime