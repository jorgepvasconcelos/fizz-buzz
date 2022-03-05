from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///teste', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
