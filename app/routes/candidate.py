from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateUpdate
from app.core.dependencies import get_db

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)

# Create Candidate Route
@router.post("/")
def create_candidate(
    request: CandidateCreate,
    db: Session = Depends(get_db)
):

    candidate = Candidate(
        name=request.name,
        email=request.email,
        phone=request.phone,
        skills=",".join(request.skills),
        experience_years=request.experience_years,
        job_id=request.job_id
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    return {"candidate": candidate, "message": "Candidate Created Successfully"}

# Get Candidates Route
@router.get("/")
def get_candidates(
    db: Session = Depends(get_db)
):

    return db.query(
        Candidate
    ).all()


from uuid import UUID

# Get Candidate Route by ID
@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: UUID,
    db: Session = Depends(get_db)
):

    return db.query(
        Candidate
    ).filter(
        Candidate.id == candidate_id
    ).first()

# Update Candidate Route
@router.patch("/{candidate_id}")
def update_candidate(
    candidate_id: UUID,
    request: CandidateUpdate,
    db: Session = Depends(get_db)
):

    candidate = db.query(
        Candidate
    ).filter(
        Candidate.id == candidate_id
    ).first()

    update_data = request.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():

        if key == "skills":
            value = ",".join(value)

        setattr(
            candidate,
            key,
            value
        )

    db.commit()

    db.refresh(candidate)

    return candidate

# Delete Candidate Route
@router.delete("/{candidate_id}")
def delete_candidate(
    candidate_id: UUID,
    db: Session = Depends(get_db)
):

    candidate = db.query(
        Candidate
    ).filter(
        Candidate.id == candidate_id
    ).first()

    db.delete(candidate)

    db.commit()

    return {
        "message": "Candidate Deleted Successfully"
    }