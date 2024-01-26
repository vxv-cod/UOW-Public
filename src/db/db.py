from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///sqlite.db")
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    # pass
    pydantic_schema = None
    def to_read_model(self) -> pydantic_schema:
        return self.pydantic_schema.model_validate(self.__dict__, from_attributes=True)

async def get_async_session():
    async with async_session_maker() as session:
        yield session
