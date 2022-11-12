#!/usr/bin/python3
# 4-cities_by_state.py
"""script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    This time, write one that is safe from MySQL injections.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306, charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT city.id, city.name, state.name 
                 FROM cities
                 INNER JOIN states
                 ON city.sate_id = state.id
                 WHERE IS NULL
                 ORDER BY cities.id")
    [print(city) for city in cur.fetchall()]

    cur.close()
    db.close()
