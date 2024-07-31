from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text, create_engine
from src.config import settings
import asyncio

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True
)
sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
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