from sqlalchemy import Date
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from . import metadata

product_dimensions_table = Table(
    'product_dimensions',
    metadata.metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('unity_of_measure', String(50)),
    Column('unity_per_pack', Integer),
    Column('pack_per_level', Integer),
    Column('level_per_pallet', Integer),
    Column('unity_area', Integer)
)