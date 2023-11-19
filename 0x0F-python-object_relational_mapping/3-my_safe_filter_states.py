#!/usr/bin/python3
'''
Wait, do you remember the previous task?
Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"
as an input?

What? Empty?

Yes, it’s an SQL injection to delete all records of a table…

Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
'''
if __name___ == "__main__":
    """
    Accessing the database hbtn_0e_0_usa to get the states
    from it
    """
    db_connect = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3]
            )

    db_cursor = db_connect.cursor()

    db_cursor.execute('SELECT * FROM states WHERE name LIKE BINARY %(name)s ORDER BY \
            states.id ASC', {'name:' argv[4]})

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
