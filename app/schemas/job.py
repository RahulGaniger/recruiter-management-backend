from pydantic import BaseModel
from typing import Optional

# Schemas for Job creation 
class JobCreate(BaseModel):
    title: str
    description: str
    skills_required: str
    location: str
    department: str
    status: Optional[str] = "OPEN"

# Schema for Job update
class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    skills_required: Optional[str] = None
    location: Optional[str] = None
    department: Optional[str] = None
    status: Optional[str] = None