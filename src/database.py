import datetime
from types import Annotated
import enum
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
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

class ProjectTypes(enum.Enum):
    """
    Docstring for ProjectTypes
    """
    str_32 = Annotated[str, 32]
    str_64 = Annotated[str, 64]
    str_256 = Annotated[str, 256]
    int_pk = Annotated[int, mapped_column(primary_key=True)]
    created_at = Annotated[
        datetime.datetime,
        mapped_column(server_default=text("TIMEZONE('uts', now())")) 
    ]
    updated_at = Annotated[
        datetime.datetime,
        mapped_column(
            server_default=text("TIMEZONE('uts', now() + interval '1 day')"),
            onupdate=datetime.datetime.now(datetime.UTC),
        ),
    ]