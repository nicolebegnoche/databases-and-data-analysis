-- Drop old data to prevent complications
DROP DATABASE IF EXISTS flowers;
CREATE DATABASE flowers;
Use flowers;


CREATE TABLE Zones(
    id INT PRIMARY KEY CHECK(CHAR_LENGTH(id) <= 2),
    lowerTemp INT NOT NULL CHECK(lowerTemp between -99 and 99),
    higherTemp INT NOT NULL CHECK(higherTemp between -99 and 99)
);  -- notice that in this statement, the primary key is declared inline...

CREATE TABLE Deliveries (
	id INT AUTO_INCREMENT,
	categ VARCHAR(5) NOT NULL,
	delSize DECIMAL(5, 3),		-- up to five digits with three decimal spaces
    PRIMARY KEY (id)
);  -- ... but you can also declare the primary key at the end

CREATE TABLE FlowersInfo (
	id INT PRIMARY KEY CHECK(CHAR_LENGTH(id) = 3),
	comName VARCHAR(30) NOT NULL,
	latName VARCHAR(35) NOT NULL,
	cZone INT NOT NULL,
	hZone INT NOT NULL,
	deliver INT,
	sunNeeds VARCHAR(255) NOT NULL,
	FOREIGN KEY (cZone) REFERENCES Zones(id),
	FOREIGN KEY (hZone) REFERENCES Zones(id),
	FOREIGN KEY (deliver) REFERENCES Deliveries(id)
);


-- The most basic way to insert values:
INSERT INTO Zones
VALUES
	(2, -50, -40),	
	(3, -40, -30),
	(4, -30, -20),
	(5, -20, -10),
	(6, -10, 0),
	(7, 0, 10),
	(8, 10, 20),
	(9, 20, 30),
	(10, 30, 40);

-- Adding values only to specified columns:  (Skip id because it's set to auto-increment)
INSERT INTO Deliveries (categ, delSize)
VALUES
	('pot', 1.500),
	('pot', 2.250),
	('pot', 2.625),
	('pot', 4.250),
	('plant', NULL),
	('bulb', NULL),
	('hedge', 18.000),
	('shrub', 24.000),
	('tree', 36.000);

-- Populate from file
LOAD DATA LOCAL INFILE 'flowers.csv'
INTO TABLE FlowersInfo
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\r\n';



/*
Other helpful 

-- Automatically increase the values in a column:
id INT NOT NULL AUTO_INCREMENT          -- to start at a certain value (like 100), use AUTO_INCREMENT=100

-- Insert a default value:
OrderDate date DEFAULT CURRENT_DATE()

-- Combine multiple checks in one line:
CONSTRAINT CHK_tablename CHECK(age >= 21 AND city='Denver')

-- Prevent identical combinations of fields from being entered:
CONSTRAINT UC_tablename UNIQUE (month, day)

-- Create a primary key from multiple columns:
CONSTRAINT PK_tablename PRIMARY KEY (first, last)

*/