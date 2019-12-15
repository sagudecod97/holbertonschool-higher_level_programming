#!/usr/bin/python3
"""
Changes the name of a State
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_change = session.query(State).filter_by(id=2).first()
    state_to_change.name = "New Mexico"
    session.commit()
