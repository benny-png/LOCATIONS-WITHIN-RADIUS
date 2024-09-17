# crud.py
from sqlalchemy.orm import Session
from models.models import RestaurantDB
from schemas.schemas import RestaurantBase

def get_restaurant(db: Session, name: str):
    return db.query(RestaurantDB).filter(RestaurantDB.name == name).first()

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RestaurantDB).offset(skip).limit(limit).all()

def create_restaurant(db: Session, restaurant: RestaurantBase):
    db_restaurant = RestaurantDB(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def update_restaurant(db: Session, name: str, restaurant: RestaurantBase):
    db_restaurant = get_restaurant(db, name)
    if db_restaurant:
        for key, value in restaurant.dict().items():
            setattr(db_restaurant, key, value)
        db.commit()
        db.refresh(db_restaurant)
    return db_restaurant

def delete_restaurant(db: Session, name: str):
    db_restaurant = get_restaurant(db, name)
    if db_restaurant:
        db.delete(db_restaurant)
        db.commit()
    return db_restaurant