-- Creates a database hbtn_0d_2
-- Creates the MySQL server user user_0d_2 with the folowing requiremets:
-- 	the user should have only SELECT privileges in the database hbtn_0d_2
-- 	the user's password shouls be set to user_0d_2_pwd
-- 	if the database already exists, the script shouldn't fail
-- 	if the user already exists, the script shouldn't fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant the user only SELECT privileges in the database, hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
