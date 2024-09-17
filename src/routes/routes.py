# api.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from geopy.distance import geodesic
from .. import crud
from ..schemas import schemas
from ..database.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def read_root():
    return {"message": "Welcome to this georadius map!"}

@router.post("/restaurants/", response_model=schemas.Restaurant)
def add_restaurant(restaurant: schemas.RestaurantBase, db: Session = Depends(get_db)):
    return crud.create_restaurant(db=db, restaurant=restaurant)

@router.get("/restaurants/", response_model=List[schemas.Restaurant])
def list_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    restaurants = crud.get_restaurants(db, skip=skip, limit=limit)
    return restaurants

@router.post("/nearby-restaurants/", response_model=List[schemas.Restaurant])
def find_nearby_restaurants(request: schemas.NearbyRequest, db: Session = Depends(get_db)):
    user_location = (request.latitude, request.longitude)
    all_restaurants = crud.get_restaurants(db)
    nearby = []

    for restaurant in all_restaurants:
        restaurant_location = (restaurant.latitude, restaurant.longitude)
        distance = geodesic(user_location, restaurant_location).kilometers

        if distance <= request.radius:
            nearby.append(restaurant)

    return nearby

@router.delete("/restaurants/{restaurant_name}")
def delete_restaurant(restaurant_name: str, db: Session = Depends(get_db)):
    db_restaurant = crud.delete_restaurant(db, name=restaurant_name)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"message": f"Restaurant '{restaurant_name}' has been deleted."}

@router.put("/restaurants/{restaurant_name}", response_model=schemas.Restaurant)
def update_restaurant(restaurant_name: str, restaurant: schemas.RestaurantBase, db: Session = Depends(get_db)):
    db_restaurant = crud.update_restaurant(db, name=restaurant_name, restaurant=restaurant)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant