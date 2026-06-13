from fastapi import APIRouter, status

from app.modules.research.schema import CreateResearchJob
from app.modules.research.tasks import start_process_research

research_router = APIRouter(prefix="/research", tags=["research"])

@research_router.post("/", status_code=status.HTTP_202_ACCEPTED)
def create_research_job(payload: CreateResearchJob):
    # Running in background
    start_process_research.delay(payload.topic) #type: ignore

    return {"message" : "research job in process"}