#!/usr/bin/python3
"""Script that links the State class to the `states` table in a database"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Base class for all models
Base = declarative_base()


class State(Base):
    """State class that maps to the 'states' table in the database."""
    __tablename__ = 'states'

    # Column definitions for the 'states' table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Ensure correct number of arguments are passed
    if len(sys.argv) != 4:
        print(
            "Usage: ./6-model_state.py mysql_username "
            "mysql_password database_name"
        )
        sys.exit(1)

    # Extract command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and bind to Base
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}'
        f'@localhost/{database_name}',
        pool_pre_ping=True
    )

    # Create all tables
    Base.metadata.create_all(engine)