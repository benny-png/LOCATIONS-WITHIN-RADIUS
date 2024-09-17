# src/database/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create a 'data' directory in the parent directory of 'src'
data_dir = os.path.join(os.path.dirname(os.path.dirname(current_dir)), 'data')
os.makedirs(data_dir, exist_ok=True)

# Use the data directory for the database file
db_file = os.path.join(data_dir, 'restaurants.db')
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_file}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()