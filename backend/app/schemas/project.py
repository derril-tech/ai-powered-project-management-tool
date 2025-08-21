from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from uuid import UUID

class ProjectBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: str = Field(default='active', pattern='^(active|completed|archived)$')

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(None, pattern='^(active|completed|archived)$')
    settings: Optional[str] = None

class ProjectResponse(ProjectBase):
    id: UUID
    owner_id: UUID
    team_id: UUID
    settings: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProjectWithStats(ProjectResponse):
    task_count: int
    completion_percentage: float
