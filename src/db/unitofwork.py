from abc import ABC, abstractmethod
from typing import Type

from db.db import async_session_maker
from repositories.repository import AutoRepository
from utils.import_models import all_models_classes


class ABCUnitOfWork(ABC):
    
    @abstractmethod
    def __init__(self):
        for name in AutoRepository.all_models_classes:
            self.__setattr__(name, Type[AutoRepository])        
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *args):
        raise NotImplementedError

    @abstractmethod
    async def commit(self):
        raise NotImplementedError

    @abstractmethod
    async def rollback(self):
        raise NotImplementedError


class UnitOfWork(ABCUnitOfWork):

    def __init__(self):
        self.session_factory = async_session_maker
    
    async def __aenter__(self):
        self.session = self.session_factory()

        for model in all_models_classes:
            repository = AutoRepository(model, self.session)
            name = repository.model_name
            self.__setattr__(name, repository)

            # print(f"getattr == {getattr(self, name) = }")

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def rollback(self):
        await self.session.rollback()

    async def commit(self):
        await self.session.commit()
