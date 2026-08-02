-- Run these directly in psql (psql -U postgres)

-- create and drop a database
CREATE DATABASE employee_db;
-- DROP DATABASE employee_db;

-- connect to it: \c employee_db

-- create table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100),
    salary NUMERIC(10,2)
);

-- insert records
INSERT INTO employees (name, department, salary) VALUES
    ('Aarav Sharma', 'Engineering', 65000),
    ('Priya Verma', 'Marketing', 52000),
    ('Rohan Gupta', 'Engineering', 70000),
    ('Sneha Reddy', 'HR', 48000);

-- select with where
SELECT * FROM employees WHERE department = 'Engineering';

-- truncate
TRUNCATE TABLE employees RESTART IDENTITY;
