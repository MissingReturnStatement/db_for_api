import requests
from src.queries.orm import SyncORM
from utils.functions import calculate_hash,calculate_cosine_similarity
import datetime
syncorm = SyncORM()
url = "http://127.0.0.1:8000/embedding"
#data = {"text": "test text"}
data = {"text":"def create_tables(): hohol Base.metadata.drop_all(sync_engine); Base.metadata.create_all(sync_engine); sync_engine.echo = True; @staticmethod; def select_all_from_embeddings(): with session_factory() as session: query = select(EmbeddingsOrm); results = session.execute(query).scalars().all(); for embedding in results: print(fID: {embedding.id}, Embedding: {embedding.embedding}, Hash: {embedding.hash}, Repo: {embedding.repo}, Date: {embedding.date}); @staticmethod; def insert_test_data(embed_data): with session_factory() as session: session.add(embed_obj); session.commit(); @staticmethod; def insert_embeddings(): with session_factory() as session: pass; async def async_insert_data(): async with async_session_factory() as session: embed = EmbeddingsOrm(embedding=some vector); session.add(embed); await session.commit() тек"}


response = requests.post(url, json=data)

embedding_data = {}

if response.status_code != 200:
    embedding = response.json()
    print('fuck')
    print(embedding)
    print("Embedding:", type(embedding))
    embedding_data['embedding'] = embedding
    embedding_data['hash'] = calculate_hash(data["text"])
    syncorm.insert_data_to_embeddings(embedding_data)
else:
    print("Error:", response.status_code, response.text)
#syncorm.select_all_from_embeddings()
table_tuple_1 = syncorm.select_by_id_from_embeddings(4)
table_tuple_2 = syncorm.select_by_id_from_embeddings(5)
print(table_tuple_2['embedding'])
result = calculate_cosine_similarity(table_tuple_1['embedding'],table_tuple_2['embedding'])
print(result," COSINE SIMILARITY")
compaired_dict = {
    "result": result.item(),
    "hash_1": table_tuple_1["hash"],
    "hash_2": table_tuple_2["hash"]
}
syncorm.insert_data_to_compaired(compaired_dict)
syncorm.select_all_from_compaired()