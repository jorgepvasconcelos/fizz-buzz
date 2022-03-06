from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///teste.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def create_database():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    # create_database()

    Session = sessionmaker(bind=engine)
    session = Session()

    u1 = User(age=14)
    session.add(u1)
    session.commit()
