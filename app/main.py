from fastapi import FastAPI

from .api.routers import library, notes
from .db import Base, engine

# Create tables automatically (simple approach)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library API")

app.include_router(library.router)
app.include_router(notes.router)


@app.get("/")
def root():
    return {"status": "ok"}
