from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.tasks import TaskSchema


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    @abstractmethod
    async def edit_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_one():
        raise NotImplementedError
    
    @abstractmethod
    async def find_all():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None
    session = None

    def __init__(self, session: AsyncSession):
        self.session = session
        # print(f'{self.model.__name__ = }')

    async def add_one(self, data: dict) -> int:
        stmt = insert(self.model).values(**data).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def edit_one(self, id: int, data: dict) -> int:
        stmt = update(self.model).values(**data).filter_by(id=id).returning(self.model.id)
        res = await self.session.execute(stmt)
        return res.scalar_one()
    
    async def find_one(self, **filter_by):
        stmt = select(self.model).filter_by(**filter_by)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()
    
    async def find_all(self: model):
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        return [row[0].to_read_model() for row in res.all()]
