"""
This file for db manager (Create, Update)
"""

from datetime import datetime
import time
from pydantic import BaseModel, Field
from typing import Optional


class TaskCreate(BaseModel):
    title: str
    description: str = None
    done: bool = False
    created_at: datetime = datetime.fromtimestamp(time.time())


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None
    created_at: Optional[datetime] = None
