# main.py
from fastapi import FastAPI
from database.database import engine
from models import models
from routes.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)