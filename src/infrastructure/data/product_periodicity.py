from sqlalchemy import MetaData
from sqlalchemy import Column, Table, Integer, String

from infrastructure.data.metadata import Metadata

product_periodicity_table = Table(
    'product_periodicity',
    Metadata().get_metadata(),
    Column('id', Integer, primary_key=True),
    Column('entry_on_warehouse', String(50)),
    Column('expire_date', String(50))
)

