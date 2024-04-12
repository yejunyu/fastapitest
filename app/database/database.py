from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

DATABASE_URL = f"mysql+mysqlconnector://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DB}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
    获取数据库会话，并在完成后关闭它。
    Args:
        无
    Returns:
        SessionLocal: 数据库会话对象。
"""
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()