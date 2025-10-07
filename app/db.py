import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def get_database_url():
    return os.getenv("DATABASE_URL", "sqlite:///./test.db")


DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


# helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
