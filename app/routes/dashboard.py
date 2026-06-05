from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.core.dependencies import get_db
from app.models.job import Job
from app.models.candidate import Candidate
from app.schemas.dashboard import TopCandidateResponse

router = APIRouter(
    prefix="/dashboard-data",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
    db: Session = Depends(get_db)
):

    total_jobs = db.query(Job).count()

    active_jobs = db.query(Job).filter(
        Job.status == "OPEN"
    ).count()

    closed_jobs = db.query(Job).filter(
        Job.status == "CLOSED"
    ).count()

    total_candidates = db.query(
        Candidate
    ).count()

    avg_score = db.query(
        func.avg(Candidate.fit_score)
    ).scalar() or 0

    high_fit_candidates = db.query(
        Candidate
    ).filter(
        Candidate.fit_score >= 80
    ).count()

    top_candidates = (
        db.query(
            Candidate.name,
            Candidate.email,
            Candidate.phone,
            Candidate.fit_score
        )
        .order_by(
            Candidate.fit_score.desc()
        )
        .limit(5)
        .all()
    )

    top_candidates_data = [
        TopCandidateResponse(
            name=candidate.name,
            email=candidate.email,
            phone=candidate.phone,
            score=candidate.fit_score
        )
        for candidate in top_candidates
    ]

    candidates_per_job = round(
        total_candidates / total_jobs,
        2
    ) if total_jobs else 0

    return {
        "total_jobs": total_jobs,
        "active_jobs": active_jobs,
        "closed_jobs": closed_jobs,
        "total_candidates": total_candidates,
        "high_fit_candidates": high_fit_candidates,
        "avg_ai_score": round(avg_score, 2),
        "candidates_per_job": candidates_per_job,
        "top_candidates": top_candidates_data
    }