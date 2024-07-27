from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker,AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from config import settings
import asyncio

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)

# async def connect_engine():
#     async with async_engine.connect() as conn:
#         res = await conn.execute(text("SELECT VERSION()"))
#         print(f"(res)")
#
async def connect_engine():
    async with async_engine.connect() as conn:
        result = await conn.execute(text("SELECT VERSION()"))
        version = result.one_or_none()  # Получение одной строки из результата
        print(f"Database version: {version[0]}")  # Вывод версии базы данных

# Запуск асинхронной функции в асинхронном цикле событий
asyncio.run(connect_engine())

#asyncio.run(connect_engine())