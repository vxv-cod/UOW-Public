from schemas.users import UserSchemaAdd
from db.unitofwork import ABCUnitOfWork, UnitOfWork


class UsersService:
    async def add_user(self, uow: ABCUnitOfWork, user: UserSchemaAdd):
        user_dict = user.model_dump()
        async with uow:
            user_id = await uow.users.add_one(user_dict)
            await uow.commit()
            return user_id

    async def get_users(self, uow: UnitOfWork):
        async with uow:
            users = await uow.users.find_all()
            return users
