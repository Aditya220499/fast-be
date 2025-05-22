from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class TodoItem(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    category: str
    priority: str = Field(..., pattern='^(Low|Medium|High)$')
    status: str = Field(..., pattern='^(Active|Completed|Archived)$')
    reminder_at: Optional[datetime] = None
    tags: List[str] = []
    attachments: List[str] = []
    is_favorite: bool = False

    # These fields will be handled by backend
    id: Optional[str] = None  # MongoDB ObjectId will be converted to string
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }