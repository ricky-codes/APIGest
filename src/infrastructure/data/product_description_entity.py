from sqlalchemy import Date, DateTime
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import BigInteger
from sqlalchemy import String
from sqlalchemy import ForeignKey

from src.infrastructure.data import metadata

product_description_table = Table(
    'product_description',
    metadata.metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('product_category_id', ForeignKey('product_category.id')),
    Column('product_subcategory_id', ForeignKey('product_subcategory.id')),
    Column('ean', BigInteger),
    Column('internal_code', BigInteger),
    Column('modified_at', DateTime),
    Column('inserted_at', DateTime),
    Column('created_at', DateTime),
    Column('product_dimensions_id', ForeignKey('product_dimensions.id')),
    Column('product_periodicity_id', ForeignKey('product_periodicity.id'))
)