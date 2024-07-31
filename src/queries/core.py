from sqlalchemy import text
from database import async_engine,sync_engine
from models import metadata_object

def create_tables():
    #metadata_object.drop_all(tables=)
    metadata_object.drop_all(sync_engine)
    #metadata_object.create_all(sync_engine)
def drop_all_tables(engine, metadata):
    with engine.connect() as conn:
        # Удаляем все зависимости через каскадное удаление
        conn.execute(text("DROP TABLE IF EXISTS model_results CASCADE"))
        conn.execute(text("DROP TABLE IF EXISTS embeddings CASCADE"))