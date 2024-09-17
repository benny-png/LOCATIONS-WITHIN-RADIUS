# GeoRadius API

This is a FastAPI-based project that provides a simple API to manage restaurants and find nearby restaurants based on a user's location and radius. The API supports creating, listing, updating, deleting restaurants, and finding restaurants within a specified radius using geographic coordinates.

## Features

- **Add a restaurant**: Add a new restaurant by providing its name and coordinates (latitude and longitude).
- **List restaurants**: Retrieve a list of restaurants, with options to paginate.
- **Find nearby restaurants**: Find restaurants within a certain radius (in **kilometers**) of a given location.
- **Update a restaurant**: Update the details of an existing restaurant.
- **Delete a restaurant**: Remove a restaurant from the list by its name.

## Endpoints

### 1. Welcome Message
- **URL**: `/`
- **Method**: `GET`
- **Response**: A simple welcome message.

#### Example Response:
```json
{
    "message": "Welcome to this georadius map!"
}
```

---

### 2. Add a Restaurant
- **URL**: `/restaurants/`
- **Method**: `POST`
- **Description**: Add a new restaurant by providing the name and coordinates (latitude and longitude).
- **Request Body**: A `RestaurantBase` object (name, latitude, longitude).
- **Response**: The newly created restaurant.

#### Example Request:
```json
{
    "name": "Pizza Palace",
    "latitude": -6.7924,
    "longitude": 39.2083
}
```

#### Example Response:
```json
{
    "id": 1,
    "name": "Pizza Palace",
    "latitude": -6.7924,
    "longitude": 39.2083
}
```

---

### 3. List Restaurants
- **URL**: `/restaurants/`
- **Method**: `GET`
- **Description**: List all restaurants with pagination options (`skip` and `limit`).
- **Response**: A list of restaurants.

#### Example Response:
```json
[
    {
        "id": 1,
        "name": "Pizza Palace",
        "latitude": -6.7924,
        "longitude": 39.2083
    },
    {
        "id": 2,
        "name": "Burger Shack",
        "latitude": -6.8000,
        "longitude": 39.2100
    }
]
```

---

### 4. Find Nearby Restaurants
- **URL**: `/nearby-restaurants/`
- **Method**: `POST`
- **Description**: Find restaurants within a specified radius (in **kilometers**) of a given location.
- **Request Body**: A `NearbyRequest` object (latitude, longitude, radius in kilometers).
- **Response**: A list of nearby restaurants within the radius.

#### Example Request:
```json
{
    "latitude": -6.7924,
    "longitude": 39.2083,
    "radius": 5  # Radius in kilometers
}
```

#### Example Response:
```json
[
    {
        "id": 1,
        "name": "Pizza Palace",
        "latitude": -6.7924,
        "longitude": 39.2083
    }
]
```

---

### 5. Update Restaurant
- **URL**: `/restaurants/{restaurant_name}`
- **Method**: `PUT`
- **Description**: Update the details of an existing restaurant by its name.
- **Request Body**: A `RestaurantBase` object (name, latitude, longitude).
- **Response**: The updated restaurant.

#### Example Request:
```json
{
    "name": "Pizza Paradise",
    "latitude": -6.7924,
    "longitude": 39.2083
}
```

#### Example Response:
```json
{
    "id": 1,
    "name": "Pizza Paradise",
    "latitude": -6.7924,
    "longitude": 39.2083
}
```

---

### 6. Delete Restaurant
- **URL**: `/restaurants/{restaurant_name}`
- **Method**: `DELETE`
- **Description**: Delete a restaurant by its name.
- **Response**: A confirmation message that the restaurant has been deleted.

#### Example Response:
```json
{
    "message": "Restaurant 'Pizza Palace' has been deleted."
}
```

## Project Structure

```
├── api.py                 # API router with all restaurant endpoints
├── crud.py                # CRUD operations for restaurant database
├── database.py            # Database setup and session management
├── schemas.py             # Pydantic models for request/response validation
```

## How to Run

1. Install the required dependencies:
    ```bash
    pip install fastapi sqlalchemy geopy uvicorn
    ```

2. Run the FastAPI app with Uvicorn:
    ```bash
    uvicorn api:router --reload
    ```

3. Visit the interactive API documentation at:
   - **Swagger UI**: `http://127.0.0.1:8000/docs`
   - **ReDoc**: `http://127.0.0.1:8000/redoc`

## Dependencies

- **FastAPI**: Web framework to build the API.
- **SQLAlchemy**: ORM for database interaction.
- **Geopy**: Library to calculate geographical distances.
- **Uvicorn**: ASGI server for running the FastAPI app.

## License

This project is licensed under the Apache 2.0 License.

