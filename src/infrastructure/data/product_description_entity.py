from sqlalchemy import Date
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from . import metadata

product_description_table = Table(
    'product_description',
    metadata.metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('category', String(100)),
    Column('subcategory', String(100)),
    Column('ean', Integer),
    Column('internal_code', String(100)),
    Column('product_dimensions_id', ForeignKey('product_dimensions.id')),
    Column('product_periodicity_id', ForeignKey('product_periodicity.id'))
)