from pydantic import BaseModel
from sqlalchemy import MetaData, Table, create_engine
from db.db import Base
from schemas.tasks import TaskSchema
from schemas.users import UserSchemaAdd
from db.unitofwork import ABCUnitOfWork, UnitOfWork
# from services.base_service import BaseService
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


# class Column(BaseModel):
#     id: int
#     type: any
#     table: str
#     primary_key: bool
#     # nullable=False


# class test(BaseModel):
#     Column: list[Column]

#     class Config:
#         from_attributes = True


class TaskSchema(BaseModel):
    id: int
    title: str
    author_id: int
    assignee_id: int

    class Config:
        from_attributes = True

class testService():
    async def get(self, uow: UnitOfWork):
        # async with uow:
        #     users = await uow.users.find_all()
        #     return users    

        engine = create_engine("sqlite+aiosqlite:///sqlite.db")
        someengine = engine
        metadata_obj = Base.metadata
        table_ = Table("tasks", metadata_obj, autoload_with=engine)
        # columns = [c.model_dump()  for c in table_.columns]
        columns = [c.__dict__  for c in table_.columns]

        # columns = [{c.name : c.type} for c in table_.columns]
        # print(columns)
        # # print(table_.__dict__)
        # tables = metadata_obj.tables
        print(columns)
        # print(table.tables)
        # return {
        #     'columns' : columns,
        #     # 'tables' : tables
        #     }
        # pydantic_schema = test

        # sss = columns[0]
        # print(sss)

        # for t in metadata_obj.sorted_tables:
        #     print(t.name)
        
        # def to_read_model(data):
        #         return TaskSchema.model_validate(data.__dict__, from_attributes=True)        
        
        # return [to_read_model(row) for row in columns]

        # return TaskSchema.model_validate(sss, from_attributes=True)

        # metadata_obj = MetaData()
        # metadata_obj.reflect(bind=engine)
        # users_table = metadata_obj.tables["users"]
        # addresses_table = metadata_obj.tables["tasks"]
        # print(users_table)
        # print(addresses_table)
