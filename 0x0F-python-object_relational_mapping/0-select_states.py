#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Accessing the database hbtn_0e_0_usa to get the states
    from it
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
            )

    db_cursor = db_connect.cursor()

    db_cursor.execute('SELECT * FROM states')

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
