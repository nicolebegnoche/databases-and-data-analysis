CREATE DATABASE hr;

USE hr;

CREATE TABLE Employees (
    id     INT PRIMARY KEY, 
    name   VARCHAR(20),
    gender CHAR(1),
    email  VARCHAR(50), 
    birth  DATE, 
    start  DATE, 
    salary INT, 
    ssn    VARCHAR(11), 
    phone  VARCHAR(12)
);