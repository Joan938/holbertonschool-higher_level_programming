#!/usr/bin/python3
"""class definition module"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(
        Integer,
        unique=True,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    state = relationship("State", backref="cities")