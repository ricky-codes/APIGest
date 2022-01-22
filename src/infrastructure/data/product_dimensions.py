from sqlalchemy import MetaData
from sqlalchemy import Column, Table, Integer, String

metadata_obj = MetaData()

product_dimensions_table = Table(
    'product_dimensions',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('unity_of_sale', String(50)),
    Column('quantity_per_pack', Integer),
    Column('pack_by_level', Integer),
    Column('level_by_pallet', Integer),
    Column('unity_area', Integer)
)