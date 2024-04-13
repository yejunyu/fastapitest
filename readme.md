> https://ktechhub.medium.com/building-a-todo-api-with-fastapi-and-sqlalchemy-a-step-by-step-guide-dbf5fe2fc7cd

Anytime you make changes to your models just run:
```
alembic upgrade head && \
alembic revision --autogenerate && \
alembic upgrade head
```