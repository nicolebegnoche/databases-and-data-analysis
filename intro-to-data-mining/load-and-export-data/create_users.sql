CREATE USER 'hr' IDENTIFIED BY '024680';
CREATE USER 'hr_admin' IDENTIFIED BY '135791';

GRANT SELECT ON TABLE Employees TO 'hr';
GRANT ALL ON TABLE Employees TO 'hr_admin';