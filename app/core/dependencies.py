from app.database.db import SessionLocal
from jose import jwt
from fastapi.security import HTTPBearer
from fastapi import Depends
from app.utils.security import SECRET_KEY
from app.models.recruiter import Recruiter
from sqlalchemy.orm import Session

security = HTTPBearer()

# Dependency to get a database session
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Dependency to get the current authenticated user
def get_current_user(
    token=Depends(security),
    db: Session = Depends(get_db)
):

    payload = jwt.decode(
        token.credentials,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    recruiter_id = payload.get("sub")

    recruiter = db.query(
        Recruiter
    ).filter(
        Recruiter.id == recruiter_id
    ).first()

    return recruiter