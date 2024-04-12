from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, func
from app.database.base_class import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), index=True)
    description = Column(String(255), nullable=True)
    is_completed = Column(Boolean, default=False)
    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def __str__(self):
        return f"Todo #{self.id}: {self.title}, Completed: {self.is_completed}"
