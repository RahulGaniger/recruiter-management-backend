# import google.generativeai as genai
# import json

# from app.core.config import settings

# GEMINI_API_KEY = settings.GEMINI_API_KEY


# genai.configure(
#     api_key=GEMINI_API_KEY
# )

# model = genai.GenerativeModel(
#     "gemini-2.5-flash"
# )

# def parse_resume(resume_text):

#     prompt = f"""
#     Extract candidate information.

#     Calculate total professional experience in years.

#     Return ONLY JSON.

#     {{
#         "name":"",
#         "email":"",
#         "phone":"",
#         "experience_years":0,
#         "skills":[]
#     }}

#     Resume:

#     {resume_text}
#     """

#     response = model.generate_content(
#         prompt
#     )

#     return json.loads(
#         response.text
#             .replace("```json", "")
#             .replace("```", "")
#             .strip()
#     )

import google.generativeai as genai
import json

from app.core.config import settings

GEMINI_API_KEY = settings.GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def parse_resume(resume_text):

    prompt = f"""
    Extract candidate information from the resume.

    Calculate total professional experience in years.

    Return ONLY valid JSON.

    {{
        "name":"",
        "email":"",
        "phone":"",
        "experience_years":0,
        "skills":[]
    }}

    Resume:

    {resume_text}
    """

    response = model.generate_content(
        prompt
    )

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(
        cleaned_response
    )


def calculate_ai_fit_score(
    job,
    candidate_data,
    resume_text
):

    prompt = f"""
    You are an AI Recruitment Assistant.

    Evaluate how well the candidate matches the job.

    Consider:

    1. Skills Match
    2. Experience Match
    3. Job Description Match
    4. Overall Profile Relevance

    Job Title:
    {job.title}

    Department:
    {job.department}

    Required Skills:
    {job.skills_required}

    Job Description:
    {job.description}

    Candidate Details:
    {candidate_data}

    Resume Text:
    {resume_text}

    Return ONLY JSON.

    {{
        "fit_score": 0,
        "fit_reason": "",
        "strengths": [],
        "weaknesses": [],
        "matched_skills": []
    }}
    """

    response = model.generate_content(
        prompt
    )

    cleaned_response = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(
        cleaned_response
    )