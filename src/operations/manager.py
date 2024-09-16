from datetime import datetime
import time
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str
    description: str = None
    done: bool = False
    created_at: datetime = datetime.fromtimestamp(time.time())
