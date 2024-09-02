import requests
from src.queries.orm import SyncORM
from utils.functions import calculate_hash
import datetime
syncorm = SyncORM()
url = "http://127.0.0.1:8000/embedding"
#data = {"text": "test text"}
data = {"text":"def create_tables(): hohol Base.metadata.drop_all(sync_engine); Base.metadata.create_all(sync_engine); sync_engine.echo = True; @staticmethod; def select_all_from_embeddings(): with session_factory() as session: query = select(EmbeddingsOrm); results = session.execute(query).scalars().all(); for embedding in results: print(fID: {embedding.id}, Embedding: {embedding.embedding}, Hash: {embedding.hash}, Repo: {embedding.repo}, Date: {embedding.date}); @staticmethod; def insert_test_data(embed_data): with session_factory() as session: session.add(embed_obj); session.commit(); @staticmethod; def insert_embeddings(): with session_factory() as session: pass; async def async_insert_data(): async with async_session_factory() as session: embed = EmbeddingsOrm(embedding=some vector); session.add(embed); await session.commit() тек"}


response = requests.post(url, json=data)

embedding_data = {}

if response.status_code == 200:
    embedding = response.json()
    print('fuck')
    print(embedding)
    print("Embedding:", type(embedding))
    embedding_data['embedding'] = embedding
    embedding_data['hash'] = calculate_hash(data["text"])
    syncorm.insert_data_to_embeddings(embedding_data)
else:
    print("Error:", response.status_code, response.text)
#syncorm.insert_test_data(str(embedding))
syncorm.select_all_from_embeddings()