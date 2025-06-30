#!/usr/bin/python3
"""
Defines the City model, which includes a foreign key to the State model.
Uses SQLAlchemy for database mapping.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City class mapped to the 'cities' table in the database.

    Attributes:
        id: Primary key and auto-incrementing integer.
        name: Name of the city (string, not null).
        state_id: Foreign key linking the city to its state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)