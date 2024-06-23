#!/usr/bin/python3
"""
An introduction to MySQLdb Python lybrary
with MySQL database.
"""
import sys

import MySQLdb


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    query = sys.argv[4]

    # connect to MySQL db
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
        )
    cur = db.cursor()

    # execute sql query
    cur.execute(
          "SELECT * FROM states WHERE name=%s",
          (query,)
        )
    states = cur.fetchall()

    # close the cursor
    cur.close()

    for state in states:
        print(state)


if __name__ == "__main__":
    main()
