from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: Optional[bool] = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    create_at: datetime
    update_at: datetime

    class Config:
        from_attributes = True
        # orm_mode = True
