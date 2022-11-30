-- Creates A database, hbtn_0d_usa & a table (on created database), states on your MySQL server
-- states description:
-- 	id INT (unique, auto-generated & can't be null) & name VARCHAR(256) that can't be null
-- If the database or table already exists, the script shouldn't fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
