#!/usr/bin/python3
"""
List the first State object
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).first()
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
