#!/usr/bin/python3
"""
A script that lists all cities of a given state from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Ensure there are exactly 4 arguments
    if len(sys.argv) != 5:
        print(
            "Usage: ./5-filter_cities.py mysql_username"
            "mysql_password database_name state_name"
        )
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:5]

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

        query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """

        # Execute the query with the state name parameter
        cur.execute(query, (state_name,))

        # Fetch all results and print cities
        cities = cur.fetchall()
        if cities:
            print(", ".join([city[0] for city in cities]))
        else:
            print("")

    except MySQLdb.MySQLError as e:
        # Handle any database connection or query errors
        print(f"Error: {e}")

    finally:
        # Close the cursor and the database connection
        if db:
            cur.close()
            db.close()