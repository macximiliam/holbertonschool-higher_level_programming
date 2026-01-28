#!/usr/bin/python3
"""
Contains the class definition of a State and an instance Base.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating the instance of Base
Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    # Column definitions
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
