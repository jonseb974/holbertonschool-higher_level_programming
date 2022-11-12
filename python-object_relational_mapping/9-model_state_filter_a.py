#!/usr/bin/python3
# 9-model_state_filter_a.py
"""Script that lists all State that contains the letter a
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


def firstState():
    """Prints first state
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains("a"))
    for state in states:
        print("{}: {}".format(state.id, state.name))
        session.close()


if __name__ == '__main__':
    firstState()
