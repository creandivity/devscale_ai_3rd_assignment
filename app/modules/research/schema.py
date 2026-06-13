from pydantic import BaseModel

class CreateResearchJob(BaseModel):
    topic: str