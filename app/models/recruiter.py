from sqlalchemy import Column, Integer, String
from app.database.base import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Recruiter(Base):

    __tablename__ = "recruiters"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String)

    email = Column(String, unique=True)

    password = Column(String)