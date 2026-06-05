from fastapi import APIRouter
from fastapi import APIRouter
from uuid import UUID
from sqlalchemy import DateTime
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.job import Job
from app.core.dependencies import get_current_user, get_db
from app.schemas.job import JobCreate, JobUpdate




router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

# Create Job Route
@router.post("/")
def create_job(
    request:JobCreate,
    db:Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    job = Job(
        title=request.title,
        description=request.description,
        skills_required=request.skills_required,
        location=request.location,
        department=request.department,
        recruiter_id=current_user.id
    )

    db.add(job)

    db.commit()

    return {
        "message":"Job Created successfully",
        "job": job
    }

# Get Jobs Route
@router.get("/")
def get_jobs(
    db:Session = Depends(get_db)
):

    return db.query(Job).all()

# Get Job Route by ID
@router.get("/{job_id}")
def get_job(
    job_id:UUID,
    db:Session = Depends(get_db)
):
    return db.query(Job).filter(
        Job.id == job_id
    ).first()

@router.patch("/{job_id}")
def update_job(
    job_id: UUID,
    request: JobUpdate,
    db: Session = Depends(get_db)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return {"message": "Job not found"}

    if request.title is not None:
        job.title = request.title

    if request.description is not None:
        job.description = request.description

    if request.skills_required is not None:
        job.skills_required = request.skills_required

    if request.location is not None:          # ✅ added
        job.location = request.location

    if request.department is not None:        # ✅ added
        job.department = request.department

    if request.status is not None:            # ✅ added
        job.status = request.status

    db.commit()
    db.refresh(job)

    return {
        "message": "Job updated successfully",
        "job": job
    }

# Close Job Route
@router.patch("/{job_id}/close")
def close_job(
    job_id:UUID,
    db:Session=Depends(get_db)
):

    job = db.query(Job).get(job_id)

    job.status = "CLOSED"

    db.commit()

    return {
        "message":"Closed"
    }

# Delete Job Route
@router.delete("/{job_id}")
def delete_job(
    job_id:UUID,
    db:Session=Depends(get_db)
):

    job = db.query(Job).get(job_id)

    db.delete(job)

    db.commit()

    return {
        "message":"Deleted"
    }