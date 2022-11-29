-- Lists the number of recoreds with the same score in the table, second_table from the hbtn_0c_0 database in the MySQL server
-- The result should display:
-- 	the score
-- 	the number of records for this score with the label number
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument of the mysql command
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
