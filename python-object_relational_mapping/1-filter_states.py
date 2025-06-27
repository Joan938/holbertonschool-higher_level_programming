#!/usr/bin/python3
"""This module filters state names by thir first letter"""
import MySQLdb
import sys


def main():
    """main function that runs the module"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database,
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM states WHERE BINARY states.name\
                LIKE 'N%' ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print("({}, '{}')".format(row[0], row[1]))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()