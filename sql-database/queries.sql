-- a) Display the total number of zones.
SELECT COUNT(id) AS 'Total Zones'
FROM Zones;


-- b) Display the number of flowers per cool zone.
SELECT cZone AS 'Cool Zone', COUNT(*) AS 'Number of Flowers'
FROM FlowersInfo
GROUP BY cZone
ORDER BY cZone;


-- c) List the common names of the plants that have delivery sizes less than 5.
SELECT comName AS 'Common Name', delSize AS 'Delivery Size'
FROM FlowersInfo
INNER JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id
WHERE delSize < 5;


-- d) List the common names and sun needs of the plants that require full sun.
--    (Plants requiring full sun have an ‘S’ in sun needs.)
SELECT comName AS 'Common Name', sunNeeds AS 'Sun Needs'
FROM FlowersInfo
WHERE sunNeeds LIKE 'S'
	OR sunNeeds LIKE 'Sto%';


-- e) List the delivery category names alphabetically without repetition.
SELECT DISTINCT categ AS 'Delivery Categories'
FROM Deliveries
ORDER BY categ ASC;


-- f) List the plants alphabetically by their common name and show the following columns:
--        Name, Cool Zone (low), Cool Zone (high), Delivery Category
SELECT
	comName AS 'Name',
	lowerTemp AS 'Cool Zone (low)',
	higherTemp AS 'Cool Zone (high)',
	categ AS 'Delivery Category'
FROM FlowersInfo f
    JOIN Deliveries d ON f.deliver = d.id
    JOIN Zones z ON f.cZone = z.id;


-- g) List the common names of plants that have the same hot zone as “Pink Caladiums”.
--    (The solution must store hot zone in a variable.)
SET @hotZone = (
	SELECT hZone
	FROM FlowersInfo
	WHERE comName='Pink Caladiums'
	);

SELECT comName AS 'Common Name'
FROM FlowersInfo
WHERE hZone = @hotZone;


/* h) Display the following statistics based on the plants that have delivery sizes:
        • total number of plants
        • minimum delivery size
        • maximum delivery size
        • average delivery size (Round to two decimals) */

SELECT
    COUNT(*) AS 'Total',
    ROUND(MIN(delSize), 1) AS 'Min',
    ROUND(MAX(delSize), 1) AS 'Max',
    ROUND(AVG(delSize), 2) AS 'Average'
FROM FlowersInfo
    INNER JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id
WHERE delSize IS NOT NULL;


-- i) Display the Latin name of the plant that has the word ‘Eyed’ in its common name.
SELECT latName AS "Latin Name"
FROM FlowersInfo
WHERE comName LIKE "%Eyed%";


-- j) List the category and common name of the plants in ascending order by category name, then common name.

SELECT
    categ AS 'Category',
    comName AS 'Common Name'
FROM FlowersInfo
    INNER JOIN Deliveries ON FlowersInfo.deliver = Deliveries.id
ORDER BY 1, 2;