#!/usr/bin/python3
# 11-model_state_insert.py
"""Script that prints the State object with the name
passed as argument from the database  hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    aux = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    add_state = State(name="Louisiana")
    session.add(add_state)
    session.commit()
    print("{}".format(add_state.id))

    session.close()
