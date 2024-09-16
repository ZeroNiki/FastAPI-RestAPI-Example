from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy.ext.declarative import declarative_base
from typing import AsyncGenerator

URL = "sqlite+aiosqlite:///./todo.db"

metadata = MetaData()
engine = create_async_engine(URL, echo=True)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    future=True,
)

Base = declarative_base()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def init_models() -> None:
    """Create tables if they don't already exist.

    In a real-life example we would use Alembic to manage migrations.
    """
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # noqa: ERA001
        await conn.run_sync(Base.metadata.create_all)
