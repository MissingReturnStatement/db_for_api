from sqlalchemy import Table,Column, Integer, String, MetaData
from sqlalchemy import DateTime, ForeignKey
metadata_object = MetaData()

embeddings_table = Table(
    'embeddings',
    metadata_object,
    Column('id',Integer, primary_key= True),
    Column('embedding',String),
    Column('hash',Integer,unique=True),
    Column('repo', String),
    Column('date',DateTime),
    )

model_results_table = Table(
    'model_result',
    metadata_object,
    Column('id',Integer,primary_key=True),
    Column('result', String),
    Column('hash_1', Integer, ForeignKey('embeddings.hash')),
    Column('hash_2', Integer, ForeignKey('embeddings.hash'))
    )