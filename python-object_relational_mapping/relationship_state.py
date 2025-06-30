#!/usr/bin/python3
"""
Defines the State model, which includes a relationship with the City model.
Uses SQLAlchemy for database mapping.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """State class mapped to the 'states' table in the database.

    Attributes:
        id: Primary key and auto-incrementing integer.
        name: Name of the state (string, not null).
        cities: Relationship with the City class.
        If a State is deleted, related Cities are also deleted.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Relationship with City. Cascade delete if a state is deleted.
    cities = relationship("City", backref="state", cascade="all, delete")