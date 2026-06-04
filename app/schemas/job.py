from pydantic import BaseModel
from typing import Optional

# Schemas for Job creation 
class JobCreate(BaseModel):
    title: str
    description: str
    skills_required: str

# Schema for Job update
class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    skills_required: Optional[str] = None