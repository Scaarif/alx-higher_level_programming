-- Lists all recoreds of the table, second_table from the hbtn_0c_0 database in the MySQL server
-- The result should display:
-- 	DON'T list rows without a name value
-- 	the score and name (in this order)
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument of the mysql command
SELECT score,name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
