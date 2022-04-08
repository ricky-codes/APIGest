from sqlalchemy import Date, DateTime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from src.infrastructure.orm.metadata import metadata_obj

product_category_table = Table(
    'product_category',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('description', String(100)),
    Column('iva', Integer),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)