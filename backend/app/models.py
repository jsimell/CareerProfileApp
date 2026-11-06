from uuid import UUID
from datetime import date
from decimal import Decimal

from pydantic import BaseModel


# Profile Models
class Profile(BaseModel):
    full_name: str | None = None
    headline: str | None = None
    location: str | None = None
    summary: str | None = None
    career_goals_description: str | None = None


class ProfileCreate(Profile):
    user_id: UUID


class ProfileResponse(Profile):
    profile_id: int
    user_id: UUID


# Work Experience Models
class WorkExperience(BaseModel):
    title: str | None = None
    company: str | None = None
    location: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    description: str | None = None


class WorkExperienceResponse(WorkExperience):
    work_experience_id: int
    profile_id: int


# Project Models
class Project(BaseModel):
    title: str | None = None
    subtitle: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    description: str | None = None
    url: str | None = None


class ProjectResponse(Project):
    project_id: int
    profile_id: int


# Skill Models
class Skill(BaseModel):
    name: str | None = None
    proficiency: str | None = None


class SkillResponse(Skill):
    skill_id: int
    profile_id: int


# Language Models
class Language(BaseModel):
    language: str | None = None
    proficiency: str | None = None


class LanguageResponse(Language):
    language_id: int
    profile_id: int


# Degree Models
class Degree(BaseModel):
    finished_date: date | None = None
    title: str | None = None
    school: str | None = None
    location: str | None = None
    gpa: Decimal | None = None
    major: str | None = None
    minor: str | None = None
    additional_information: str | None = None


class DegreeResponse(Degree):
    degree_id: int
    profile_id: int


# Hobby Models
class Hobby(BaseModel):
    name: str | None = None
    description: str | None = None


class HobbyResponse(Hobby):
    hobby_id: int
    profile_id: int


# Project-Skill Association Models
class ProjectSkill(BaseModel):
    project_id: int
    skill_id: int
