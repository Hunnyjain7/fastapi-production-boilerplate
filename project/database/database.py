from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:@localhost:3306/fastapi_boilerplate"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_database_session():
    try:
        print("db opened")
        data_base = SessionLocal()
        yield data_base
    finally:
        print("db closed")
        data_base.close() # noqa

