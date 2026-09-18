from datetime import datetime
from typing import Optional
import uuid

from pydantic import BaseModel, Field, ConfigDict


class ClickSchema(BaseModel):
    click_id: uuid.UUID
    offer: Optional[str] = Field(None, max_length=255)
    sub1: Optional[str] = Field(None, max_length=1000)
    timestamp: datetime
    ip: Optional[str] = Field(None, max_length=45)
    user_agent: Optional[str] = Field(None, max_length=2000)

    model_config = ConfigDict(from_attributes=True)

