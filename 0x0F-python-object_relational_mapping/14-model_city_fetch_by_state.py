#!/usr/bin/python3
"""
Prints all the cities into the DB
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State
import sys

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(city.name, city.id, state.name))
