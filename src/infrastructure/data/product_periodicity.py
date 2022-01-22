from sqlalchemy import MetaData
from sqlalchemy import Column, Table, Integer, String

metadata_obj = MetaData()

product_periodicity_table = Table(
    'product_periodicity',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('entry_on_warehouse', String(50)),
    Column('expire_date', String(50))
)

