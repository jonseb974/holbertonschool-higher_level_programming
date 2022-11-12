#!/usr/bin/python3
# 5-filter_cities.py
"""a script that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT c.name \
                 FROM cities AS c \
                 INNER JOIN states AS s \
                 ON c.state_id=s.id \
                 WHERE s.name = %s \
                 ORDER BY c.id ASC;", (argv[4],))

    [print(state) for state in cur.fetchall()]

    cur.close()
    db.close()
