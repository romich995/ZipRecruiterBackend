import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import UUID, String, DateTime, Index

from src.db import Base

class Click(Base):
    __tablename__ = "clicks"

    click_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    offer: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    sub1: Mapped[Optional[str]] = mapped_column(
        String(1000),
        nullable=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    ip: Mapped[Optional[str]] = mapped_column(
        String(45),
        nullable=True,
    )

    user_agent: Mapped[Optional[str]] = mapped_column(
        String(2000),
        nullable=True,
    )

index = Index("idx_timestamp",Click.timestamp.desc())