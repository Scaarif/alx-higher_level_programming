-- Creates a table second_table in the database hbtn_0c_0 in the MySQL server
-- and adds multiple rows
-- the database name will be passed as argument of mysql command
-- If the table, second_table already exists, the script shouldn't fail
-- NOT allowed to use the SELECT and SHOW statements
-- Also creates a few records
CREATE TABLE IF NOT EXISTS second_table (
	id INT, name VARCHAR(256), score INT
	);
INSERT INTO second_table VALUES(1, 'John', 10);
INSERT INTO second_table VALUES(2, 'Alex', 3);
INSERT INTO second_table VALUES(3, 'Bob', 14);
INSERT INTO second_table VALUES(4, 'George', 8);
