#!/usr/bin/python3
"""List all states in a MySQL database."""
import MySQLdb
import sys

if __name__ == "__main__":
    # grab credentials and database name from argv
    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]

    # connect to the MySQL server on localhost:3306
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db,
        charset="utf8"
    )
    cur = conn.cursor()

    # execute the required query
    cur.execute("SELECT * FROM states ORDER BY id ASC;")

    # fetch and print each row as a tuple
    for row in cur.fetchall():
        print(row)

    # clean up
    cur.close()
    conn.close()
