import datetime

from sqlalchemy import text,Table,Column, Integer, String, MetaData
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base

class EmbeddingsOrm(Base):
    __tablename__ = 'embeddings'
    id: Mapped[int] = mapped_column(primary_key=True)
    embedding: Mapped[str]
    hash: Mapped[int] = mapped_column(unique=True)
    repo: Mapped[str | None]
    date: Mapped[datetime.datetime] = mapped_column(server_default=text("timezone('utc',now())"))

class CompairedPairOrm(Base):
    __tablename__ = 'compaired_pair'
    id: Mapped[int] = mapped_column(primary_key=True)
    result: Mapped[str]
    hash_1: Mapped[int] = mapped_column(ForeignKey("embeddings.hash",ondelete="CASCADE"))
    hash_2: Mapped[int] = mapped_column(ForeignKey("embeddings.hash",ondelete="CASCADE"))
