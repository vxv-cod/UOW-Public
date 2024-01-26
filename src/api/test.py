__all__ = ['router']
from fastapi import APIRouter

# from api.dependencies import UOWDep
from dependencies import UOWDep

# from schemas.users import UserSchemaAdd
from services.test import testService

# print(f"{__name__ = }")

router = APIRouter(
    prefix="/test",
    tags=["Test"],
)


@router.get("")
async def get(
    uow: UOWDep,
):
    users = await testService().get(uow)
    return users
