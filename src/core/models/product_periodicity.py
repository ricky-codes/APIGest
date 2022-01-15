from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.schema import ForeignKey

from core.models.base import Base

class Product_Periodicity(Base):
    __tablename__ = "Product_Periodicity"

    ID = Column(Integer, primary_key = True)
    entry_warehouse = Column(DateTime)
    expire_date = Column(DateTime)