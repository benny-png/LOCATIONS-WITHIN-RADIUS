# schemas.py
from pydantic import BaseModel

class RestaurantBase(BaseModel):
    name: str
    latitude: float
    longitude: float

class Restaurant(RestaurantBase):
    class Config:
        orm_mode = True

class NearbyRequest(BaseModel):
    latitude: float
    longitude: float
    radius: float