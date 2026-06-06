
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from uuid import UUID
import uuid
import os
from app.core.dependencies import get_db
from app.models.candidate import Candidate
from app.models.job import Job
from app.services.resume_parser import extract_resume_text
from app.services.ai_parser import parse_resume
from app.services.fit_score import calculate_fit_score

router = APIRouter(
    prefix="/analyze",
    tags=["Analyze"]
)

# Analyze Resume Route
@router.post("/analyze")
async def analyze_resume(
    job_id: UUID = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    filename = f"{uuid.uuid4()}.pdf"

    file_path = f"uploads/{filename}"

    contents = await resume.read()

    with open(file_path, "wb") as file:
        file.write(contents)

    # Extract Resume Text
    resume_text = extract_resume_text(
        file_path
    )

    # Parse Resume Using Gemini
    parsed_data = parse_resume(
        resume_text
    )

    # Fetch Job
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if not job:
        return {
            "message": "Job not found"
        }

    # Calculate AI Fit Score
    fit_result = calculate_fit_score(
        job,
        parsed_data,
        resume_text
    )

    # Create Fit Reason
    fit_reason = fit_result.get(
        "fit_reason",
        ""
    )

    # Save Candidate
    candidate = Candidate(
        name=parsed_data.get("name"),
        email=parsed_data.get("email"),
        phone=parsed_data.get("phone"),
        skills=",".join(
            parsed_data.get(
                "skills",
                []
            )
        ),
        experience_years=parsed_data.get(
            "experience_years",
            0
        ),
        fit_score=fit_result.get(
            "fit_score",
            0
        ),
        fit_reason=fit_reason,
        resume_path=file_path,
        job_id=job_id
    )

    db.add(candidate)

    db.commit()

    db.refresh(candidate)

    return {
        "message":
            "Candidate analyzed and saved successfully",

        "candidate_id":
            str(candidate.id),

        "candidate_name":
            candidate.name,

        "fit_score":
            candidate.fit_score,

        "fit_reason":
            candidate.fit_reason,

        "matched_skills":
            fit_result.get(
                "matched_skills",
                []
            ),

        "strengths":
            fit_result.get(
                "strengths",
                []
            ),

        "weaknesses":
            fit_result.get(
                "weaknesses",
                []
            ),

        "resume_path":
            candidate.resume_path
    }