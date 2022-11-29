-- Creates a tavle called first_table in the current database in the MySQL server
-- the database name will be passed as argument of mysql command
-- if the table already exists, the script shouldn't fail.
-- first_table description:
-- id INT
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
