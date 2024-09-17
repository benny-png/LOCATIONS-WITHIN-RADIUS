# models.py
from sqlalchemy import Column, Float, String
from ..database.database import Base

class RestaurantDB(Base):
    __tablename__ = "restaurants"

    name = Column(String, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)