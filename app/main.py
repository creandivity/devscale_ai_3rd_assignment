from fastapi import FastAPI, Depends
from scalar_fastapi import get_scalar_api_reference
from sqlmodel import Session, select

from app.models.database import Todo
from app.models.engine import get_session
from app.modules.research.router import research_router

app = FastAPI()

# @app.get("/todos")
# def get_todos(db: Session = Depends(get_session)):
#     todos = db.exec(select(Todo))
#     return todos

# @app.get("/todos/{id}")
# def get_todo(id: int, db: Session = Depends(get_session)):
#     todo = db.get(Todo, id)
#     return todo

app.include_router(research_router) # type: ignore

@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(title="FastAPI Research", openapi_url="/openapi.json")