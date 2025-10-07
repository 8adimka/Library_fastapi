from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .core import DATABASE_URL

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment")

# sync engine (простая конфигурация)
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
