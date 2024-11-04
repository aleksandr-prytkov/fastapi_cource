from fastapi import APIRouter
from fastapi import Depends
from typing import Optional, Annotated

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# tasks = []


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
