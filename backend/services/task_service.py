from typing import Dict
from typing import Optional
from models.task import Task


tasks: Dict[str, Task] = {}


def create_task(task: Task) -> Task:
    tasks[task.task_id] = task
    return task


def get_task(task_id: str) -> Optional[Task]:
    return tasks.get(task_id)