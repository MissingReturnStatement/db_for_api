from sqlalchemy import text,insert
from database import sync_engine, async_engine, session_factory, async_session_factory
from models import metadata_object, EmbeddingsOrm, CompairedPairOrm, Base
def create_tables():
    #sync_engine.echo = False
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True

def select_all():
    with session_factory() as session:
        session.get()
# def drop_all_tables(engine, metadata):
#     with engine.connect() as conn:
#         # Удаляем все зависимости через каскадное удаление
#         conn.execute(text("DROP TABLE IF EXISTS model_results CASCADE"))
#         conn.execute(text("DROP TABLE IF EXISTS embeddings CASCADE"))

def insert_data():
    embed = EmbeddingsOrm(embedding = "some vector")
    with session_factory() as session:
        session.add(embed)
        session.commit()

async def async_insert_data():
    async with async_session_factory() as session:
        embed = EmbeddingsOrm(embedding="some vector")
        session.add(embed)
        await session.commit()