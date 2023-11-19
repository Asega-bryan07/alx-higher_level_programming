#!/usr/bin/python3
'''
a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    accesses the database to select the cities
    '''
    db_connect = db.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    with db_connect.cursor() as db_cursor:
        db_cursor.execute(
                """
                SELECT cities.id, cities.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC
                """, {
                    'state_name': argv[4]
                    }
                )
        rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
