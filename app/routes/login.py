from app.schemas.auth import LoginRequest
from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.utils.security import (
    verify_password,
    create_access_token
)
from app.core.dependencies import get_db
from app.models.recruiter import Recruiter
from fastapi import HTTPException

router = APIRouter(
    prefix="/login",
    tags=["Login"]
)

# Login Route
@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    recruiter = db.query(
        Recruiter
    ).filter(
        Recruiter.email == request.email
    ).first()

    if not recruiter:
        raise HTTPException(
            status_code=404,
            detail="Recruiter account does not exist"
        )

    if not verify_password(
        request.password,
        recruiter.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "sub": str(recruiter.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "Bearer",
        "recruiter_id": str(recruiter.id)
    }