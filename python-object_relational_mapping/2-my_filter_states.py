#!/usr/bin/python3
""" Filter states by user input """

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command-line arguments
    username, password, database, state_name = sys.argv[1:5]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query with case-sensitive comparison
    query = (
        "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"
        .format(state_name)
    )
    cur.execute(query)

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and connection
    cur.close()
    db.close()