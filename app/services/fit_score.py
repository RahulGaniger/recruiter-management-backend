# def calculate_fit_score(
#     candidate_skills,
#     job_skills_string
# ):

#     job_skills = {
#         skill.strip().lower()
#         for skill in job_skills_string.split(",")
#     }

#     candidate_skills = {
#         skill.strip().lower()
#         for skill in candidate_skills
#     }

#     matched_skills = (
#         job_skills.intersection(
#             candidate_skills
#         )
#     )

#     score = (
#         len(matched_skills)
#         / len(job_skills)
#     ) * 100

#     return {
#         "score": round(score, 2),
#         "matched_skills": list(
#             matched_skills
#         )
#     }

from app.services.ai_parser import (
    calculate_ai_fit_score
)

def calculate_fit_score(
    job,
    candidate_data,
    resume_text
):
    return calculate_ai_fit_score(
        job,
        candidate_data,
        resume_text
    )