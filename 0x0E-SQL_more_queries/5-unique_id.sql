-- Creates a table, unique_id on your MySQL server
-- unique_id description:
-- 	id INT (UNIQUE)	with DEFAULT value 1 & name VARCHAR(256)
-- If the table already exists, the script shouldn't fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT '1' UNIQUE, name VARCHAR(256));
