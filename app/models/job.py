from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Job(Base):

    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    title = Column(String)

    description = Column(String)

    skills_required = Column(String)

    status = Column(String, default="OPEN")

    recruiter_id = Column(
        UUID(as_uuid=True),
        ForeignKey("recruiters.id")
    )