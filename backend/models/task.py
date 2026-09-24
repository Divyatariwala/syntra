from enum import Enum
from pydantic import BaseModel
from typing import Optional


class TaskStatus(str, Enum):
    CREATED = "created"
    PLANNING = "planning"
    PLANNED = "planned"
    EXECUTING = "executing"
    COMPLETED = "completed"
    FAILED = "failed"

class Task(BaseModel):
    task_id: str
    objective: str
    status: TaskStatus
    plan: Optional[dict] = None
    result: Optional[dict] = None
    evaluation: Optional[dict] = None
    error: Optional[str] = None