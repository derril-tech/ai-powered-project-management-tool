from sqlalchemy import Column, String, Text, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.models.base import Base, TimestampMixin, UUIDMixin

class Sprint(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "sprints"
    
    # Sprint information
    name = Column(String(255), nullable=False)
    goal = Column(Text, nullable=True)
    status = Column(String(50), default='planning', nullable=False)  # planning, active, completed
    
    # Sprint timeline
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    
    # Relationships
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    
    project = relationship("Project", back_populates="sprints")
    tasks = relationship("Task", back_populates="sprint")
    
    # Indexes
    __table_args__ = (
        Index('idx_sprints_project_id', 'project_id'),
        Index('idx_sprints_status', 'status'),
        Index('idx_sprints_start_date', 'start_date'),
        Index('idx_sprints_end_date', 'end_date'),
    )
    
    @validates('status')
    def validate_status(self, key, value):
        if value not in ['planning', 'active', 'completed']:
            raise ValueError('Invalid sprint status')
        return value
    
    @validates('end_date')
    def validate_end_date(self, key, value):
        if value and value <= self.start_date:
            raise ValueError('End date must be after start date')
        return value
    
    @property
    def is_active(self):
        return self.status == 'active'
    
    @property
    def is_completed(self):
        return self.status == 'completed'
    
    @property
    def duration_days(self):
        return (self.end_date - self.start_date).days
    
    @property
    def task_count(self):
        return len(self.tasks)
    
    @property
    def completion_percentage(self):
        if not self.tasks:
            return 0
        completed = len([t for t in self.tasks if t.status == 'done'])
        return (completed / len(self.tasks)) * 100
