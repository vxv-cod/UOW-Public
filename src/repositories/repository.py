import sys
from db.db import Base
from .base_repository import SQLAlchemyRepository

from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

class AutoRepository(SQLAlchemyRepository):
    def __init__(self, model: BaseModel, session: AsyncSession):
        self.model = model
        self.session = session
        self.model_name = f'{model.__name__}'.lower()

    # def __str__(self):
    #     # return f"{dir(self.model)}"
    #     return f"{self.model.__name__}Repository"
    
    # __repr__ = __str__
    
    # def __name__(self):
    #     return f"{self.model.__name__}Repository"

        # print(f"--{__name__}-------{self.model.__name__}Repository")
        # print(f"---------{self.model.__tablename__}Repository")