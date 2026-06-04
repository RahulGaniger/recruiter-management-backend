from fastapi import FastAPI
from app.database.db import engine
from app.database.base import Base
from app.routes.auth import router as auth_router
from app.routes.job import router as job_router
from app.routes.login import router as login_router
from app.routes.candidate import router as candidate_router
from app.models.recruiter import Recruiter
from app.models.job import Job
from app.models.candidate import Candidate

app = FastAPI()

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(login_router)
app.include_router(candidate_router)

Base.metadata.create_all(bind=engine)