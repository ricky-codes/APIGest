from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import ForeignKey

from core.models.base import Base

class Product_Description(Base):
    __tablename__ = "Product_Description"

    ID = Column(Integer, primary_key = True)
    name = Column(String(200))
    category = Column(String(200))
    subcategory = Column(String(200))
    ean = Column(Integer)
    internal_code = Column(Integer)