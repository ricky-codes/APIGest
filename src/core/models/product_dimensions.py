from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.sql.schema import ForeignKey

from core.models.base import Base

class Product_Dimensions(Base):
    __tablename__ = "Product_Dimensions"

    ID = Column(Integer, primary_key = True)
    unity_of_sale = Column(Enum)
    quantity_per_pack = Column(Integer)
    pack_by_level = Column(Integer)
    level_by_pallet = Column(Integer)
    unity_area = Column(Enum)