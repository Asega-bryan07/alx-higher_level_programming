--  a script that lists all records of the table second_table of the database hbtn_0c_0
SELECT * FROM score, name FROM second_table WHERE name IS NOT NULL AND != '' ORDER BY score DESC;
