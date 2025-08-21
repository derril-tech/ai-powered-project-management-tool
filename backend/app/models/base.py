from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()

class TimestampMixin:
    """Mixin to add created_at and updated_at timestamps to models."""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class UUIDMixin:
    """Mixin to add UUID primary key to models."""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

class SoftDeleteMixin:
    """Mixin to add soft delete functionality to models."""
    deleted_at = Column(DateTime, nullable=True)
    
    @property
    def is_deleted(self):
        return self.deleted_at is not None
