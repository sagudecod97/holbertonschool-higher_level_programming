#!/usr/bin/python3
"""
Creates a state that inherits from Base
"""


from sys import argv
import MySQLdb
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Define class State """

    __tablename__ = "states"

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
