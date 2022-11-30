-- Creates a table, force_name on your MySQL server
-- force_name description:
-- 	id INT & name VARCHAR(256) cant't be null
-- If the table already exists, the script shouldn't fail
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
