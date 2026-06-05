import uuid
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from app.database.base import Base
from sqlalchemy import Float
from sqlalchemy import Column, DateTime
from datetime import datetime

class Candidate(Base):

    __tablename__ = "candidates"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    resume_path = Column(String)
    skills = Column(String)
    experience_years = Column(Float, nullable=False)
    fit_score = Column(Float)
    fit_reason = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    job_id = Column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id")
    )