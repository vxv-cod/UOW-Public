__all__ = ['router']
from fastapi import APIRouter

from dependencies import UOWDep
from schemas.tasks import TaskSchemaAdd, TaskSchemaEdit
from services.tasks import TasksService

# print(f"{__name__ = }")

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)


@router.post("")
async def add_task(task: TaskSchemaAdd, uow: UOWDep,):
    task_id = await TasksService().add_task(uow, task)
    return {"task_id": task_id}


@router.get("")
async def get_tasks(uow: UOWDep):
    return await TasksService().get_tasks(uow)


@router.get("/history")
async def get_task_history(
    uow: UOWDep,
):
    tasks = await TasksService().get_task_history(uow)
    return tasks



@router.patch("/{id}")
async def edit_task(
    uow: UOWDep,
    id: int,
    task: TaskSchemaEdit,
):
    await TasksService().edit_task(uow, id, task)
    return {"ok": True}
