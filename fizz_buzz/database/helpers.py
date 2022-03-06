from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from models import engine


@contextmanager
def create_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()


def insert_obj(obj):
    with create_session() as session:
        session.add(obj)
        session.flush()
        session.commit()


def select_obj_by_id(obj, id):
    with create_session() as session:
        resultado = session.query(obj).filter_by(id=id).first()
        session.close()
        return resultado


def update_obj_by_id(obj, id, objUpdate):
    with create_session() as session:
        session.query(obj).filter_by(id=id).update(objUpdate)
        session.flush()
        session.commit()
        session.close()
