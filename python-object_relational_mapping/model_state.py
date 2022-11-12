#!/usr/bin/python3
"""
Start link class to table in database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent database Class."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(Strin(128), nullable=False)
