#!/usr/bin/python3
"""
List all State objects that contains an 'a' into the name
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter(State.name == sys.argv[4])

    if instance is None:
        print("Not found")
    else:
        print("{}".format(instance[0].id))
