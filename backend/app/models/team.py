from sqlalchemy import Column, String, Text, Index
from sqlalchemy.orm import relationship
from app.models.base import Base, TimestampMixin, UUIDMixin

class Team(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "teams"
    
    # Team information
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    
    # Team settings
    settings = Column(String(1000), nullable=True)  # JSON string for team settings
    
    # Relationships
    users = relationship("User", back_populates="team")
    projects = relationship("Project", back_populates="team")
    
    # Indexes
    __table_args__ = (
        Index('idx_teams_name', 'name'),
    )
