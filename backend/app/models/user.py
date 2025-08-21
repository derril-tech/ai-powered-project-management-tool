from sqlalchemy import Column, String, Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base, TimestampMixin, UUIDMixin

class User(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "users"
    
    # User information
    email = Column(String(255), nullable=False, unique=True, index=True)
    name = Column(String(255), nullable=False)
    avatar = Column(String(500), nullable=True)
    
    # Authentication
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
    
    # Role and permissions
    role = Column(String(50), default='contributor', nullable=False)  # owner, admin, pm, contributor, viewer
    
    # Team relationship
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id"), nullable=False)
    
    # Relationships
    team = relationship("Team", back_populates="users")
    owned_projects = relationship("Project", back_populates="owner", foreign_keys="Project.owner_id")
    assigned_tasks = relationship("Task", back_populates="assignee", foreign_keys="Task.assignee_id")
    
    # Constraints and indexes
    __table_args__ = (
        UniqueConstraint('email', name='uq_users_email'),
        Index('idx_users_team_id', 'team_id'),
        Index('idx_users_role', 'role'),
    )
    
    @property
    def is_admin(self):
        return self.role in ['owner', 'admin']
    
    @property
    def is_project_manager(self):
        return self.role in ['owner', 'admin', 'pm']
