import sys
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserSchema


class Users(Base):
    __tablename__ = "users"
    pydantic_schema = UserSchema

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


# module = sys.modules[__name__]
# models_classes = [value for value in (getattr(module, name) for name in dir(module)) 
#            if isinstance(value, type) and getattr(value, '__module__') == module.__name__
# ]
# print(f'{__name__} == {models_classes = }')