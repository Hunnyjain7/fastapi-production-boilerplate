import os
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_url = os.environ.get('DATABASE_URL')
engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database_session() -> Generator:
    try:
        data_base = SessionLocal()
        yield data_base
    finally:
        data_base.close()  # noqa
