-- If we want to delete all records that passes a certain condition we can use:
-- Syntax: DELETE FROM table
--         [WHERE condition]

-- If we 'forget' the `WHERE` clause then all the records of the table are going to be deleted

-- Database: world
CREATE TABLE copy_country AS SELECT * FROM country;
CREATE TABLE copy_city AS SELECT * FROM city;

-- Deleting all countries from Asia (first the cities)
DELETE FROM copy_city
WHERE CountryCode IN (
	SELECT Code
    FROM country
	WHERE Continent = "Asia"
    )
;
DELETE FROM copy_country
WHERE Continent = "Asia"
;

SELECT * FROM copy_city;
SELECT * FROM copy_country;

-- Never Do:
DELETE FROM copy_city;

SELECT * FROM copy_city;

DROP TABLE copy_country;
DROP TABLE copy_city;




