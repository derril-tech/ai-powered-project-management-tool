# Backend Models Development Guidelines

## Overview

This directory contains SQLAlchemy database models for the AI-Powered Project Management Tool backend.

## Directory Structure

```
models/
├── __init__.py             # Model imports
├── base.py                 # Base model with common fields
├── user.py                 # User and authentication models
├── project.py              # Project and team models
├── task.py                 # Task and sprint models
├── automation.py           # Automation and workflow models
├── ai.py                   # AI integration models
└── _INSTRUCTIONS.md        # This file
```

## Model Development Rules

### 1. File Naming
- Use snake_case for model files: `user.py`, `project.py`
- Use PascalCase for model classes: `User`, `Project`

### 2. Model Structure
```python
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.models.base import Base

class Project(Base):
    __tablename__ = "projects"
    
    # Primary key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Required fields
    name = Column(String(255), nullable=False)
    description = Column(Text)
    
    # Foreign keys
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    
    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    owner = relationship("User", back_populates="owned_projects")
    team = relationship("Team", back_populates="projects")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
```

### 3. Field Types
- Use `UUID` for primary keys and foreign keys
- Use `String(255)` for short text fields
- Use `Text` for long text fields
- Use `DateTime` for timestamps
- Use `Boolean` for boolean fields
- Use `Integer` for numeric fields
- Use `JSON` for complex data structures

### 4. Relationships
- Define relationships with `relationship()`
- Use `back_populates` for bidirectional relationships
- Use `cascade` options appropriately
- Use `lazy="select"` for default loading
- Use `lazy="joined"` for frequently accessed relationships

### 5. Constraints and Indexes
```python
from sqlalchemy import Index, UniqueConstraint

class User(Base):
    __tablename__ = "users"
    
    # Unique constraints
    __table_args__ = (
        UniqueConstraint('email', name='uq_users_email'),
        Index('idx_users_email', 'email'),
        Index('idx_users_team_id', 'team_id'),
    )
```

### 6. Soft Deletes
```python
class SoftDeleteMixin:
    deleted_at = Column(DateTime, nullable=True)
    
    @property
    def is_deleted(self):
        return self.deleted_at is not None
```

## Common Patterns

### Base Model
```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime
from datetime import datetime

Base = declarative_base()

class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
```

### Many-to-Many Relationships
```python
# Association table
project_members = Table(
    'project_members',
    Base.metadata,
    Column('project_id', UUID(as_uuid=True), ForeignKey('projects.id'), primary_key=True),
    Column('user_id', UUID(as_uuid=True), ForeignKey('users.id'), primary_key=True),
    Column('role', String(50), nullable=False, default='member'),
    Column('joined_at', DateTime, default=datetime.utcnow),
)

class Project(Base):
    # ... other fields ...
    members = relationship("User", secondary=project_members, back_populates="projects")
```

### Polymorphic Relationships
```python
from sqlalchemy import Column, String, Integer

class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String(50), nullable=False)
    subject_id = Column(UUID(as_uuid=True), nullable=False)
    subject_type = Column(String(50), nullable=False)
    
    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'activity'
    }
```

## Database Migrations

### Creating Migrations
```bash
# Generate migration
alembic revision --autogenerate -m "Add project model"

# Apply migration
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Migration Best Practices
- Always review auto-generated migrations
- Test migrations on development data
- Include rollback instructions
- Use descriptive migration names
- Test both upgrade and downgrade

## Validation and Business Logic

### Model Validation
```python
from sqlalchemy.orm import validates

class Task(Base):
    # ... fields ...
    
    @validates('priority')
    def validate_priority(self, key, value):
        if value not in ['low', 'medium', 'high', 'urgent']:
            raise ValueError('Invalid priority level')
        return value
    
    @validates('due_date')
    def validate_due_date(self, key, value):
        if value and value < datetime.utcnow():
            raise ValueError('Due date cannot be in the past')
        return value
```

### Business Logic Methods
```python
class Project(Base):
    # ... fields and relationships ...
    
    @property
    def is_active(self):
        return self.status == 'active'
    
    @property
    def task_count(self):
        return len(self.tasks)
    
    @property
    def completion_percentage(self):
        if not self.tasks:
            return 0
        completed = len([t for t in self.tasks if t.status == 'done'])
        return (completed / len(self.tasks)) * 100
    
    def add_member(self, user, role='member'):
        # Business logic for adding members
        pass
```

## Performance Considerations

### Query Optimization
- Use `lazy="selectin"` for collections
- Use `lazy="joined"` for single relationships
- Avoid N+1 queries with proper eager loading
- Use database indexes for frequently queried fields

### Bulk Operations
```python
from sqlalchemy.orm import Session

def bulk_create_tasks(session: Session, tasks_data: List[dict]):
    tasks = [Task(**data) for data in tasks_data]
    session.add_all(tasks)
    session.commit()
```

## Testing

### Model Tests
```python
import pytest
from app.models.project import Project
from app.models.user import User

def test_project_creation():
    user = User(email="test@example.com", name="Test User")
    project = Project(
        name="Test Project",
        description="Test Description",
        owner=user
    )
    
    assert project.name == "Test Project"
    assert project.owner == user
    assert project.is_active is True
```

## TODO Items

- [ ] Create base model with common fields
- [ ] Implement User and Team models
- [ ] Create Project and Task models
- [ ] Build Sprint and SprintTask models
- [ ] Implement Automation models
- [ ] Create AI integration models
- [ ] Add proper indexes and constraints
- [ ] Implement soft delete functionality
- [ ] Add model validation
- [ ] Create database migrations
- [ ] Add comprehensive test coverage
- [ ] Implement audit logging
- [ ] Add data encryption for sensitive fields
