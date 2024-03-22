-- Setup for MySQL server
-- Script to automate setup

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
GRANT ALL ON hbnb_dev_db.* TO 'root'@'localhost';
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;