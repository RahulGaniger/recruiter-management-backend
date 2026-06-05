from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime
from datetime import datetime

class Job(Base):

    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title = Column(String)

    description = Column(String)

    location = Column(String, nullable=False)

    department = Column(String, nullable=False)

    skills_required = Column(String)

    status = Column(String, default="OPEN")

    

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    recruiter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recruiters.id")
    )