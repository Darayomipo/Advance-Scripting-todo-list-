from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import datetime

import models
from models import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all domains, adjust as necessary for security
    # allow_credentials=True,
    # allow_methods=["*"],  # This allows all HTTP methods
    # allow_headers=["*"],  # This allows all headers
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#crud-utils
#gets all todos
@app.get("/todos/")
def read_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()

@app.post("/todos/")
def create_todo(request_data: dict, db: Session = Depends(get_db)):
    title = request_data["title"]
    description = request_data["description"]
    status = request_data["status"]
    priority = request_data["priority"]
    created = datetime.now()
    date_completed = request_data["date_completed"]
    
    todo = models.Todo(title=title, description=description, status=status, priority=priority,created = created, date_completed= date_completed)
    db.add(todo)
    db.commit()
    return todo

error ="Task Not Found"

@app.get("/todos/{todo_id}")
def read_todo(todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo is None:
        return error
    return todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    # Fetch the todo item to be deleted
    todo_to_delete = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if todo_to_delete is None:
        raise error

    # Delete the item
    db.delete(todo_to_delete)
    db.commit()
    return "Todo item deleted successfully"