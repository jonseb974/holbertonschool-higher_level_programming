#!/usr/bin/python3
"""Script that prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1],
        argv[2],
        argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    try:
        state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
