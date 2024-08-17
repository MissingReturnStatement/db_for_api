import hashlib

text = "def create_tables(): Base.metadata.drop_all(sync_engine); Base.metadata.create_all(sync_engine); sync_engine.echo = True; @staticmethod; def select_all_from_embeddings(): with session_factory() as session: query = select(EmbeddingsOrm); results = session.execute(query).scalars().all(); for embedding in results: print(fID: {embedding.id}, Embedding: {embedding.embedding}, Hash: {embedding.hash}, Repo: {embedding.repo}, Date: {embedding.date}); @staticmethod; def insert_test_data(embed_data): with session_factory() as session: session.add(embed_obj); session.commit(); @staticmethod; def insert_embeddings(): with session_factory() as session: pass; async def async_insert_data(): async with async_session_factory() as session: embed = EmbeddingsOrm(embedding=some vector); session.add(embed); await session.commit() тек"

def calculate_hash(text):
    hasher = hashlib.md5()
    hasher.update(text.encode('utf-8'))  # Преобразование строки в байты
    text_hash = hasher.hexdigest()
    extract_number = lambda s: int(''.join(filter(str.isdigit, s))) if any(char.isdigit() for char in s) else None
    text_hash = extract_number(text_hash)
    return int((str(text_hash))[:7])
