from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import DeclarativeMeta


class CustomBase:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


Base: DeclarativeMeta = declarative_base(cls=CustomBase)
