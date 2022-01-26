from sqlalchemy import ForeignKey
from sqlalchemy import Column, Table, Integer, String

from infrastructure.data.metadata import Metadata

product_description_table = Table(
    'product_description',
    Metadata().get_metadata(),
    Column('id', Integer, primary_key=True),
    Column('name', String(200)),
    Column('category', String(100)),
    Column('subcategory', String(100)),
    Column('ean', Integer),
    Column('internal_code', Integer)
)