from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI(
    title="Syntra API",
    description="Backend API for the Syntra agentic AI platform",
    version="0.1.0",
)


class TaskRequest(BaseModel):
    objective: str


class TaskResponse(BaseModel):
    task_id: str
    objective: str
    status: str


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "syntra-api",
    }


@app.post("/api/tasks", response_model=TaskResponse)
def create_task(request: TaskRequest):
    task_id = str(uuid4())

    return TaskResponse(
        task_id=task_id,
        objective=request.objective,
        status="received",
    )