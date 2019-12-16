#!/usr/bin/python3
"""
Defines a class City that Inherits from Base
"""


from model_state import Base
import MySQLdb
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ Defines the class City """
    __tablename__ = "cities"

    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
