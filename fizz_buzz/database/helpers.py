from contextlib import contextmanager

from sqlalchemy.orm import sessionmaker

from models import engine, User


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


def select_obj_by_id(obj, obj_id):
    with create_session() as session:
        resultado = session.query(obj).filter_by(id=obj_id).first()
        session.close()
        return resultado


def update_obj_by_id(obj, obj_id, obj_update):
    with create_session() as session:
        session.query(obj).filter_by(id=obj_id).update(obj_update)
        session.flush()
        session.commit()
        session.close()


if __name__ == '__main__':
    ...
    # ------------------------------------- how to use -------------------------------------

    # ------------------------------------- how to select -------------------------------------
    # var = select_obj_by_id(obj=User, obj_id=2)
    # print(var)

    # ------------------------------------- how to update -------------------------------------
    # update_obj_by_id(obj=User, obj_id=2,
    #                  obj_update={User.name: 'zabuza',
    #                              User.age: 50})
