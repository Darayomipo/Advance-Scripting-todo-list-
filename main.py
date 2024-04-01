from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

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


#gets all todos
@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.post("/todos/")
def create_todo(request_data: dict, db: Session = Depends(get_db)):
    title = request_data["title"]
    description = request_data["description"]
    todo = models.Todo(title=title, description=description)
    db.add(todo)
    db.commit()
    return todo