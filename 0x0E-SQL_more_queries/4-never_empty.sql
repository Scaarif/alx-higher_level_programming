-- Creates a table, id_not_null on your MySQL server
-- id_not_null description:
-- 	id INT with DEFAULT value 1 & name VARCHAR(256)
-- If the table already exists, the script shouldn't fail
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT '1', name VARCHAR(256));
