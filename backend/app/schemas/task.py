from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime
from uuid import UUID

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    status: str = Field(default='todo', pattern='^(todo|in_progress|review|done)$')
    priority: str = Field(default='medium', pattern='^(low|medium|high|urgent)$')
    estimated_hours: Optional[int] = Field(None, ge=0)
    due_date: Optional[datetime] = None

class TaskCreate(TaskBase):
    project_id: UUID
    assignee_id: Optional[UUID] = None
    sprint_id: Optional[UUID] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[str] = Field(None, pattern='^(todo|in_progress|review|done)$')
    priority: Optional[str] = Field(None, pattern='^(low|medium|high|urgent)$')
    estimated_hours: Optional[int] = Field(None, ge=0)
    actual_hours: Optional[int] = Field(None, ge=0)
    due_date: Optional[datetime] = None
    assignee_id: Optional[UUID] = None
    sprint_id: Optional[UUID] = None

class TaskResponse(TaskBase):
    id: UUID
    project_id: UUID
    assignee_id: Optional[UUID] = None
    sprint_id: Optional[UUID] = None
    actual_hours: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class TaskWithDetails(TaskResponse):
    project_name: str
    assignee_name: Optional[str] = None
    sprint_name: Optional[str] = None
    is_overdue: bool
    progress_percentage: int
