from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from database import sync_engine, async_engine, session_factory, async_session_factory
from models import metadata_object, EmbeddingsOrm, CompairedPairOrm, Base
import datetime
class SyncORM:
    @staticmethod
    def create_tables():
        #sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True
    @staticmethod
    def select_all_from_embeddings():
        with session_factory() as session:
            query = select(EmbeddingsOrm)
            results = session.execute(query).scalars().all()
            #print(f"{embeddings}")
            for embedding in results:
                print(f"ID: {embedding.id}, Embedding: {embedding.embedding}, Hash: {embedding.hash}, Repo: {embedding.repo}, Date: {embedding.date}")

    @staticmethod
    def insert_test_data(embed_data):
        with session_factory() as session:
            embed_obj = EmbeddingsOrm(
                embedding=embed_data['embedding'],
                hash=embed_data['hash'],
                repo=embed_data.get('repo'),  # Используем get чтобы безопасно достать значение
                date=embed_data.get('date', datetime.datetime.now())  # Дата по умолчанию текущее время
            )
            session.add(embed_obj)
            session.commit()

    @staticmethod
    def insert_embeddings():
        with session_factory() as session:
            pass

async def async_insert_data():
    async with async_session_factory() as session:
        embed = EmbeddingsOrm(embedding="some vector")
        session.add(embed)
        await session.commit()