# coding : utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine("mysql://root:root@127.0.0.1/dating_place?charset=utf8")
db_session =scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base=declarative_base()
Base.query=db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)