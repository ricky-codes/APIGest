from sqlalchemy import Date, DateTime, table
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import ForeignKey

from src.infrastructure.data.metadata import metadata_obj

product_subcategory_table = Table(
    'product_subcategory',
    metadata_obj,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('description', String(100)),
    Column('product_category_id', ForeignKey('product_category.id')),
    Column('modified_at', DateTime),
    Column('inserted_at', DateTime),
    Column('created_at', DateTime)
)