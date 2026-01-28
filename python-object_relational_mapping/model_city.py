#!/usr/bin/python3
"""
This file defines the City class.
It links to the cities table in the database.
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class that inherits from Base.
    It has a relationship with the State class through state_id.
    """
    __tablename__ = 'cities'

    # Auto-generated ID, unique and primary key.
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # Name of the city, max 128 characters.
    name = Column(String(128), nullable=False)

    # Link to the states table.
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
