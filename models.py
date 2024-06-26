# https://www.geeksforgeeks.org/fastapi-sqlite-databases/?ref=header_search
# https://www.geeksforgeeks.org/datetime-timezone-in-sqlalchemy/
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
# Define the database URL, change './test.db' to your actual database path
DATABASE_URL = "sqlite:///./test.db"

# Create an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class
Base = declarative_base()

# Use the Base class to define your models/entities
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(Integer, index=True)
    priority = Column(String, index=True)
    created = Column(DateTime, default = datetime.datetime.now())
    date_completed = Column(String, index=True)

# Create tables in the database
Base.metadata.create_all(bind=engine)