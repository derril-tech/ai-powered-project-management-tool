from sqlalchemy import Column, String, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base, TimestampMixin, UUIDMixin

class Project(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "projects"
    
    # Project information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default='active', nullable=False)  # active, completed, archived
    
    # Project settings
    settings = Column(String(1000), nullable=True)  # JSON string for project settings
    
    # Relationships
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    
    owner = relationship("User", back_populates="owned_projects", foreign_keys=[owner_id])
    team = relationship("Team", back_populates="projects")
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
    sprints = relationship("Sprint", back_populates="project", cascade="all, delete-orphan")
    
    # Indexes
    __table_args__ = (
        Index('idx_projects_owner_id', 'owner_id'),
        Index('idx_projects_team_id', 'team_id'),
        Index('idx_projects_status', 'status'),
    )
    
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
