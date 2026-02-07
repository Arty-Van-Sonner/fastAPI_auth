from types import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

echo = True

sync_engine = create_engine(
    url=settings.DATABASE_USL_psycopg,
    echo=echo,
)

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=echo,
)

class Base(DeclarativeBase):
    '''
    Docstring for Base
    '''
    type_annotation_map = {}

sync_session = sessionmaker(sync_engine)
async_session = async_sessionmaker(async_engine)