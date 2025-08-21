from sqlalchemy import Column, String, Text, Integer, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship, validates
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from app.models.base import Base, TimestampMixin, UUIDMixin

class Task(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "tasks"
    
    # Task information
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(String(50), default='todo', nullable=False)  # todo, in_progress, review, done
    priority = Column(String(50), default='medium', nullable=False)  # low, medium, high, urgent
    
    # Time tracking
    estimated_hours = Column(Integer, nullable=True)
    actual_hours = Column(Integer, nullable=True)
    due_date = Column(DateTime, nullable=True)
    
    # Relationships
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    sprint_id = Column(UUID(as_uuid=True), ForeignKey("sprints.id"), nullable=True)
    
    project = relationship("Project", back_populates="tasks")
    assignee = relationship("User", back_populates="assigned_tasks", foreign_keys=[assignee_id])
    sprint = relationship("Sprint", back_populates="tasks")
    
    # Indexes
    __table_args__ = (
        Index('idx_tasks_project_id', 'project_id'),
        Index('idx_tasks_assignee_id', 'assignee_id'),
        Index('idx_tasks_sprint_id', 'sprint_id'),
        Index('idx_tasks_status', 'status'),
        Index('idx_tasks_priority', 'priority'),
        Index('idx_tasks_due_date', 'due_date'),
    )
    
    @validates('priority')
    def validate_priority(self, key, value):
        if value not in ['low', 'medium', 'high', 'urgent']:
            raise ValueError('Invalid priority level')
        return value
    
    @validates('status')
    def validate_status(self, key, value):
        if value not in ['todo', 'in_progress', 'review', 'done']:
            raise ValueError('Invalid status')
        return value
    
    @validates('due_date')
    def validate_due_date(self, key, value):
        if value and value < datetime.utcnow():
            raise ValueError('Due date cannot be in the past')
        return value
    
    @property
    def is_overdue(self):
        if not self.due_date:
            return False
        return self.due_date < datetime.utcnow() and self.status != 'done'
    
    @property
    def progress_percentage(self):
        status_progress = {
            'todo': 0,
            'in_progress': 50,
            'review': 75,
            'done': 100
        }
        return status_progress.get(self.status, 0)
