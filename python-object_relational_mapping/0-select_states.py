#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
            user=argv[1],
            passwd=argv[2],
            db=argv[3], port=3306,
            charset="utf8")
    cur = db.cursor ()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in auery_rows:
        print(row)

    cur.close ()
    db.close ()
