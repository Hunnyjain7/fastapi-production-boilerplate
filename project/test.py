# from typing import Union, Optional
# import schema
# from database.database import SessionLocal, Base, Engine
# # from models import Base
# from fastapi import FastAPI
# # from sqlalchemy.orm import Session
#
# Base.metadata.create_all(bind=Engine)
#
#
# def get_database_session():
#     try:
#         data_base = SessionLocal()
#         yield data_base
#     finally:
#         data_base.close()
#
#
# app = FastAPI()


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# DatabaseUrl = "mysql+mysqlconnector://root@localhost:3306/fenced_db"
#
# Engine = create_engine(
#     DatabaseUrl, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
#
# Base = declarative_base()


# update user

# st = "it is Good"
# print(st.title())
from datetime import datetime, timedelta

time = str(datetime.now())
print(time)
print(datetime.fromisoformat(time) + timedelta(days=30))
# print(time.split('.')[0].replace('-', '/'))
# print(datetime.strptime(time.split('.')[0].replace('-', '/'), '%y/%m/%d %H:%M:%S'))
# print(datetime.strptime(time, '%d/%m/%y %H:%M:%S') - timedelta(days=30))
