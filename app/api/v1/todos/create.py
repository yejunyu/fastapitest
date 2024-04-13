from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.todo import Todo
from app.schemas.todo import TodoCreate
from app.schemas.todo import Todo as TodoSchema

router = APIRouter()


@router.post("/todos", response_model=TodoSchema)
async def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
