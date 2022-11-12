#!/usr/bin/python3
"""A script that lists all State objects from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    firstStates()
    """List all the states.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    try:
        state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
