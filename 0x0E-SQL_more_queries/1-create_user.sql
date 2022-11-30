-- Creates the MySQL server user user_0d_1 with the folowing requiremets:
-- 	the user should have all privileges of the MySQL server
-- 	the user's password shouls be set to user_0d_1_pwd
-- 	if the user already exists, the script shouldn't fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant the user all privileges in the server (global privileges)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
