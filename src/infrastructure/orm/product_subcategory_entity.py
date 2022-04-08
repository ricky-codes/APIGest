from sqlalchemy import Date, DateTime, table
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import ForeignKey

from src.infrastructure.orm.metadata import metadata_obj

product_subcategory_table = Table(
    'product_subcategory',
    metadata_obj,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('description', String(100)),
    Column('modified_at', DateTime),
    Column('created_at', DateTime),
    Column('product_category_id', Integer, ForeignKey('product_category.id', ondelete='cascade')),
    Column('product_subcategory_id', Integer, ForeignKey('product_subcategory.id', ondelete='cascade'))
)