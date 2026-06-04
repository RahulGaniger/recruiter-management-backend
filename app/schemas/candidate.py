from pydantic import BaseModel
from uuid import UUID
from typing import Optional




class CandidateCreate(BaseModel):

    name: str
    email: str
    phone: str
    skills: list[str]
    experience_years: float
    job_id: UUID


class CandidateUpdate(BaseModel):

    name: Optional[str] = None

    email: Optional[str] = None

    phone: Optional[str] = None

    skills: Optional[list[str]] = None

    experience_years: Optional[float] = None