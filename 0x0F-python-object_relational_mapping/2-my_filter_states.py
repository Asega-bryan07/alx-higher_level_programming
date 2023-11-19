#!/usr/bin/python3
'''
a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
'''
import MySQLdb as db
from sys import argv

"""
accessing the db to get all the states with the names
"""
if __name___ == "__main__":
    """
    Accessing the database hbtn_0e_0_usa to get the states from it
    """
    db_connect = MySQLdb.connect(
	    host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
	    )

    db_cursor = db_connect.cursor()

    db_cursor.execute('SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY \
	    states.id ASC'.format(argv[4]))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
	print(row)
