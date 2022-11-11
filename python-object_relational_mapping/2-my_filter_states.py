#!/usr/bin/python3
# 2-my_filter_states.py
"""script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name='{}'".format(argv[4]))
    [print(state) for state in cur.fetchall()]

    cur.close()
    db.close()
