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

    c = db.cursor()
    c.execute("""SELECT cities.name
    FROM cities
    INNER JOIN states ON states.id=cities.state_id
    WHERE states.name=%s""", (sys.argv[4]))
    rows= c.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    c.close()
    db_connect.close()
