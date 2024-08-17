from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text,delete
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
    def select_by_id_from_embeddings(id: int):
        with session_factory() as session:
            statement = select(EmbeddingsOrm).where(EmbeddingsOrm.id == id)
            result = session.execute(statement).scalar_one_or_none()
            if result:
                embedding_dict = {
                    'id': result.id,
                    'embedding': result.embedding,
                    'hash': result.hash,
                    'repo': result.repo,
                    'date': result.date
                }
                return embedding_dict
            else:
                return None
    @staticmethod
    def select_by_hash_from_embeddings(hash: int):
        with session_factory() as session:
            statement = delete(EmbeddingsOrm).where(EmbeddingsOrm.hash == hash)
            result = session.execute(statement).scalar_one_or_none()
            if result:
                embedding_dict = {
                    'id': result.id,
                    'embedding': result.embedding,
                    'hash': result.hash,
                    'repo': result.repo,
                    'date': result.date
                }
                return embedding_dict
            else:
                return None

    @staticmethod
    def insert_data_to_embeddings(embed_data: dict):
       if embed_data['hash'] != SyncORM.select_by_hash()['hash']:
           with session_factory() as session:
            embed_obj = EmbeddingsOrm(
                embedding=embed_data['embedding'],
                hash=embed_data['hash'],
                repo=embed_data.get('repo'),
                date=embed_data.get('date', datetime.datetime.now())
            )
            session.add(embed_obj)
            session.commit()
       else:
           return SyncORM.select_by_hash()['hash']
    @staticmethod
    def delete_by_id_from_embeddings(id: int):
        with session_factory() as session:
            embed = session.query(EmbeddingsOrm).filter(EmbeddingsOrm.id == id).first()
            if embed:
                session.delete(embed)
                session.commit()
            else:
                pass
                #можно какое-то логирование добавить
    @staticmethod
    def delete_by_hash_from_embeddings(hash: int):
        with session_factory() as session:
            embed = session.query(EmbeddingsOrm).filter(EmbeddingsOrm.hash == hash).first()
            if embed:
                session.delete(embed)
                session.commit()
            else:
                pass

