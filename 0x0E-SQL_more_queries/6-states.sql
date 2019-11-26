-- Creates a DB and a table, with an unique id, auto generated and can´t be NULL and
-- is a primary key, name can't be NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT AUTO_INCREMENT PRIMARY KEY UNIQUE, name VARCHAR(256) NOT NULL);
