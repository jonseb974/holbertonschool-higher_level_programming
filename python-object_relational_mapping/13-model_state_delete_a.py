#!/usr/bin/python3
# 13-model_state_delete_a.py
"""Script that prints the State object with the name
passed as argument from the database  hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
