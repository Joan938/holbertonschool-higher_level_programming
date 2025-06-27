#!/usr/bin/python3
"""
A script that lists all cities from the database `hbtn_0e_4_usa`
sorted by cities.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure there are exactly 3 arguments
    if len(sys.argv) != 4:
        print(
            "Usage: ./4-cities_by_state.py "
            "mysql_username mysql_password database_name"
        )
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1:4]

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cur = db.cursor()

        # SQL query to select cities and their respective states
        query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
        """

        # Execute the query and fetch all results
        cur.execute(query)
        rows = cur.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.MySQLError as e:
        # Handle any database connection or query errors
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        if db:
            cur.close()
            db.close()