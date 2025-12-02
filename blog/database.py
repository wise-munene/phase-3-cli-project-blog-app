# blog/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file
DATABASE_URL = "sqlite:///blog.db"

# Create the engine (connects Python to the database)
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal will be used to interact with the database
SessionLocal = sessionmaker(bind=engine)

# Base class that all models will inherit from
Base = declarative_base()
