#!/usr/bin/python3
"""
All cities by state
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE (SELECT states.id FROM \
    states WHERE states.name = %s) = cities.state_id;", (argv[4],))

    rows = cur.fetchall()

    for i in range(len(rows)):
        if i != (len(rows) - 1):
            print("{:s}, ".format(rows[i][0]), end="")
        else:
            print(rows[i][0])

    cur.close()
    db.close()
