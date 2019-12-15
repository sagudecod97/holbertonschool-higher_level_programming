#!/usr/bin/python3
"""
Deletes all object with name containing 'a'
"""

from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%'))\
                                        .order_by(State.id).all():
        session.delete(instance)

    session.commit()
    session.close()
