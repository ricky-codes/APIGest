from sqlalchemy import Date, DateTime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from src.infrastructure.orm import metadata

product_periodicity_table = Table(
    'product_periodicity',
    metadata.metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('entry_on_warehouse', Date),
    Column('expire_date', Date),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)