#!/usr/bin/python3
'''
a script that lists all cities from the database hbtn_0e_4_usa

Your script should take 3 arguments: mysql username, mysql password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    accesses the database to get the cities
    '''
    db_connect = db.connect(host="localhost", port=3306, user=argv[1],passwd=argv[2], db=argv[3])
    with db_connect.cursor() as db_cursor:
        db_cursor.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")

        rows_Selected = db_cursor.fetchall()

    if rows_selected is not None:
        for row in rows_selected:
            print(row)
