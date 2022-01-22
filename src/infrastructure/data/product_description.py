from sqlalchemy import ForeignKey, MetaData
from sqlalchemy import Column, Table, Integer, String

metadata_obj = MetaData()

product_description_table = Table(
    'product_description',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(200)),
    Column('category', String(100)),
    Column('subcategory', String(100)),
    Column('ean', Integer),
    Column('internal_code', Integer)
)