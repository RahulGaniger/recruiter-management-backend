# schemas/dashboard.py

from pydantic import BaseModel

class TopCandidateResponse(BaseModel):
    name: str
    email: str
    phone: str
    score: float