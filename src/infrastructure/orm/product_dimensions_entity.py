from sqlalchemy import Date, DateTime, Enum
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from src.core.models.product_dimensions_model import UnityOfMeasure

from src.infrastructure.orm import metadata

product_dimensions_table = Table(
    'product_dimensions',
    metadata.metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('unity_of_measure', Enum(UnityOfMeasure)),
    Column('unity_per_pack', Integer),
    Column('pack_per_level', Integer),
    Column('level_per_pallet', Integer),
    Column('unity_area', Integer),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)