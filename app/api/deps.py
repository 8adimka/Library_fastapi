from fastapi import Depends
from sqlalchemy.orm import Session

from ..db import get_db


def get_db_dep(db=Depends(get_db)) -> Session:
    return db
