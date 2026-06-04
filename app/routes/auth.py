from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from app.schemas.auth import RegisterRequest
from app.models.recruiter import Recruiter
from app.core.dependencies import get_db
from app.utils.security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    request:RegisterRequest,
    db:Session = Depends(get_db)
):

    recruiter = Recruiter(
        name=request.name,
        email=request.email,
        password=hash_password(
            request.password
        )
    )

    db.add(recruiter)

    db.commit()

    return {
        "message":"Registered"
    }