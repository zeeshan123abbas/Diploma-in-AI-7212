-- create_db.sql
-- Run in the MySQL command-line client:
--   mysql -u root -p
--   SOURCE create_db.sql;

CREATE DATABASE IF NOT EXISTS campus_db;
USE campus_db;

CREATE TABLE IF NOT EXISTS students (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(50)  NOT NULL,
    city    VARCHAR(30),
    marks   INT CHECK (marks BETWEEN 0 AND 100)
);

INSERT INTO students (name, city, marks) VALUES
    ('Ali',   'Karachi', 78),
    ('Sara',  'Lahore',  91),
    ('Bilal', 'Multan',  64);

-- A separate user for the Python app (safer than using root)
CREATE USER IF NOT EXISTS 'campus_app'@'localhost' IDENTIFIED BY 'Campus@123';
GRANT SELECT, INSERT, UPDATE, DELETE ON campus_db.* TO 'campus_app'@'localhost';

SHOW TABLES;
SELECT * FROM students;
