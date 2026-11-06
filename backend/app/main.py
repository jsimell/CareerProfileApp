from fastapi import FastAPI

from app.routers import (
    work_experiences,
)
from app.routers import degrees, hobbies, languages, profiles, project_skills, projects, skills, users

app = FastAPI()

app.include_router(profiles.router)
app.include_router(users.router)
app.include_router(work_experiences.router)
app.include_router(degrees.router)
app.include_router(projects.router)
app.include_router(skills.router)
app.include_router(languages.router)
app.include_router(hobbies.router)
app.include_router(project_skills.router)


# Root Endpoint
@app.get("/")
async def root():
    return {"message": "This is the Career Profile API!"}
