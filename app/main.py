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
from fastapi.middleware.cors import CORSMiddleware
from app.routes.upload import router as upload_router

app = FastAPI()

origins = [
    "http://localhost:5173",  # Vite React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(login_router)
app.include_router(candidate_router)
app.include_router(upload_router)

Base.metadata.create_all(bind=engine)