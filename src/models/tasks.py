import importlib
import sys
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.tasks import TaskHistorySchema, TaskSchema
from schemas.tasks import TaskHistorySchema, TaskSchema


class Tasks(Base):
    __tablename__ = "tasks"
    pydantic_schema = TaskSchema

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    # def to_read_model(self) -> schema:
    #     return self.schema.model_validate(self.__dict__, from_attributes=True)


class TaskHistory(Base):
    __tablename__ = "task_history"
    pydantic_schema = TaskHistorySchema

    id: Mapped[int] = mapped_column(primary_key=True)
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    
    previous_assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    new_assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


# import inspect
 
# classes = [cls_name for cls_name, cls_obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(cls_obj)]
# print(f'{classes = }')


module = sys.modules[__name__]
models_classes = [value for value in (getattr(module, name) for name in dir(module)) 
           if isinstance(value, type) and getattr(value, '__module__') == module.__name__
]
# print(f'{__name__} == {models_classes = }')

# xxx = []
# for name in dir(module):
#     value = getattr(module, name)
#     if isinstance(value, type) and value.__module__ == module.__name__:
#         xxx.append(value)

# print(f'task_py == {xxx = }')
