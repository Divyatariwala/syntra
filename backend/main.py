from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from agents.planner import create_plan
from models.task import Task, TaskStatus
from services.task_service import create_task as save_task, get_task
from agents.executor import execute_plan
from agents.evaluator import evaluate_result


app = FastAPI(
    title="Syntra API",
    description="Backend API for the Syntra agentic AI platform",
    version="0.1.0",
)


class TaskRequest(BaseModel):
    objective: str

class PlanStep(BaseModel):
    id: int
    description: str
    type: str

class Plan(BaseModel):
    goal: str
    steps: list[PlanStep]

class TaskResponse(BaseModel):
    task_id: str
    objective: str
    status: str
    plan: Plan


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "syntra-api",
    }


@app.post("/api/tasks", response_model=Task)
def create_task(request: TaskRequest):
    task_id = str(uuid4())

    task = Task(
        task_id=task_id,
        objective=request.objective,
        status=TaskStatus.CREATED,
    )

    save_task(task)

    task.status = TaskStatus.PLANNING

    plan = create_plan(request.objective)

    task.plan = plan
    task.status = TaskStatus.PLANNED

    return task

@app.get("/api/tasks/{task_id}", response_model=Task)
def get_task_endpoint(task_id: str):
    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task

@app.post("/api/tasks/{task_id}/execute", response_model=Task)
def execute_task(task_id: str):
    task = get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    if task.plan is None:
        raise HTTPException(
            status_code=400,
            detail="Task has no plan",
        )

    task.status = TaskStatus.EXECUTING

    try:
        result = execute_plan(task.plan)

        task.result = result

        evaluation = evaluate_result(result)

        task.evaluation = evaluation

        if evaluation["success"]:
            task.status = TaskStatus.COMPLETED
        else:
            task.status = TaskStatus.FAILED

    except Exception as exc:
        task.error = str(exc)
        task.status = TaskStatus.FAILED

    return task