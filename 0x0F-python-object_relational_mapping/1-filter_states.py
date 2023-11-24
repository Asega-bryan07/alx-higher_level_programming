#!/usr/bin/python3
"""
a script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb as db
from sys import argv

"""
accessing the db to get all the states with the names
"""
if __name___ == "__main__":
    """
        Accessing the database hbtn_0e_0_usa to get the states
        from it
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
            )

    db_cursor = db_connect.cursor()

    db_cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "N%" ORDER BY \
                    states.id ASC')

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
        db_cursor.close()
        db_connect.close()
