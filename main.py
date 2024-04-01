from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import models
from models import SessionLocal, engine

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()
