# Recruiter Management System Backend

AI-powered Recruiter Management System built using FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT Authentication, and Docker.

## Features

### Authentication

* Recruiter Registration
* Recruiter Login
* JWT-based Authentication
* Password Hashing using bcrypt
* Protected API Endpoints

### Recruiter Management

* Create Recruiter Account
* Manage Recruiter Profiles

### Job Management

* Create Jobs
* List Jobs
* Update Jobs
* Close Jobs
* Delete Jobs

### Candidate Management

* Create Candidates
* List Candidates
* Get Candidate Details
* Update Candidate Information
* Delete Candidates

### Database Management

* PostgreSQL Database
* SQLAlchemy ORM
* Alembic Migrations
* UUID-based Primary Keys
* Resume Upload
* Resume Parsing
* AI-powered Candidate Screening
* Candidate Fit Score Calculation
* Dockerized Deployment

---

## Project Structure

```text
app/

├── main.py

├── core/
│   ├── config.py
│   ├── dependencies.py
│   └── security.py

├── database/
│   ├── base.py
│   └── db.py

├── models/
│   ├── recruiter.py
│   ├── job.py
│   └── candidate.py

├── schemas/
│   ├── auth.py
│   ├── recruiter.py
│   ├── job.py
│   └── candidate.py

├── routes/
│   ├── auth.py
│   ├── recruiter.py
│   ├── job.py
│   └── candidate.py

├── services/

├── utils/

├── uploads/

alembic/
requirements.txt
.env.example
README.md
```

---

## Tech Stack

### Backend

* FastAPI
* Python

### Database

* PostgreSQL
* SQLAlchemy ORM

### Authentication

* JWT Authentication
* Passlib (bcrypt)

### Database Migration

* Alembic

### API Documentation

* Swagger UI
* OpenAPI

---

## Installation

### Clone Repository

```bash
git clone https://github.com/RahulGaniger/recruiter-management-backend.git

cd recruiter-management-backend
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the backend root directory and copy the values from `.env.example`.

Example:

```env
DATABASE_URL=your_database_url
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```

For resume parsing and candidate fit scoring, the application uses the Google Gemini API. Obtain an API key and add it to the `.env` file before running the application.

---

## Database Migration

Generate Migration:

```bash
alembic revision --autogenerate -m "initial migration"
```

Apply Migration:

```bash
alembic upgrade head
```

Check Current Migration:

```bash
alembic current
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

Application URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc Documentation:

```text
http://localhost:8000/redoc
```

---

## Authentication Flow

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

Returns JWT Access Token.

### Authorized Requests

```http
Authorization: Bearer <access_token>
```

---

## API Endpoints

### Authentication

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |

### Jobs

| Method | Endpoint             |
| ------ | -------------------- |
| POST   | /jobs                |
| GET    | /jobs                |
| PATCH  | /jobs/{job_id}       |
| PATCH  | /jobs/{job_id}/close |
| DELETE | /jobs/{job_id}       |

### Candidates

| Method | Endpoint                   |
| ------ | -------------------------- |
| POST   | /candidates                |
| GET    | /candidates                |
| GET    | /candidates/{candidate_id} |
| PATCH  | /candidates/{candidate_id} |
| DELETE | /candidates/{candidate_id} |

---

## Database Design

### Recruiters

```text
id (UUID)
name
email
password
```

### Jobs

```text
id (UUID)
title
description
skills_required
status
recruiter_id
```

### Candidates

```text
id (UUID)
name
email
phone
resume_path
skills
experience_years
fit_score
fit_reason
job_id
```

---

## Security

* Passwords are hashed using bcrypt.
* JWT Authentication secures protected endpoints.
* UUIDs are used as primary keys.
* Environment variables are used for sensitive configuration.

---

## Author

Rahul Ganiger

Built as part of a Full Stack Developer (AI SaaS Platform) technical assessment using FastAPI and PostgreSQL.
