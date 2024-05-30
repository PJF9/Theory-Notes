-- MySQL porvide us a way to change the values and modify a record
-- Syntax: UPDATE table_name
--         SET column1 = value1 [, column2 = value2 [, ...]]
--  	   [WHERE condition]

-- It is going to update (modify) the reocords that pass the condition with the new
--   data (values) that we are passing in `SET`
-- If we skip `WHERE` then all the records are going to be modified

-- For safety reasons MySQL dont allow to update if in the condition is not based
-- 	 the primary key.
-- To desable this option: Edit->Preferences->SQl Editor then unckeck 'Safe Update' then reload workbench

UPDATE favorite_countries
SET continent = "Asia", Region = "Middle East"
WHERE name REGEXP "^P"
;

UPDATE favorite_countries
SET continent = "Asia"
;


-- Database: classicmoders
-- 'Pamela Castillo' fired. All her customers must pass to 'Diane Murphy'
CREATE TABLE copy_customers AS
	SELECT *
    FROM customers
;
CREATE TABLE copy_employees AS
	SELECT *
    FROM employees
;
UPDATE copy_customers
SET salesRepEmployeeNumber = (
	SELECT employeeNumber
	FROM employees
    WHERE firstName = "Diane" AND lastName = "Murphy"
	)
WHERE salesRepEmployeeNumber = (
	SELECT employeeNumber
    FROM employees
    WHERE firstName = "Pamela" AND lastName = "Castillo"
	)
;
SELECT (
	SELECT CONCAT(e.firstName, " ", e.lastName)
    FROM employees e
    WHERE e.employeeNumber = ce.employeeNumber
	) AS fullName, COUNT(*) AS "customers"
FROM copy_customers cc JOIN copy_employees ce
	ON cc.salesRepEmployeeNumber = ce.employeeNumber
GROUP BY ce.employeeNumber
ORDER BY 2 DESC
;

DROP TABLE copy_customers;
DROP TABLE copy_employees;

-- Database: world
-- Barbados renamed in Bim, update `city` and `country`
CREATE TABLE copy_city AS
	SELECT *
    FROM city
;
CREATE TABLE copy_country AS
	SELECT *
	FROM country
;
UPDATE copy_city
SET countryCode = "BIM"
WHERE CountryCode = (
	SELECT Code
    FROM copy_country
    WHERE Name = "Barbados"
	)
;
UPDATE copy_country
SET Code = "Bim"
WHERE Code = (
	SELECT Code
    FROM country
    WHERE Name = "Barbados"
    )
;
SELECT ccn.Code, ccn.Name, COUNT(*) AS Cities
FROM copy_city cct JOIN copy_country ccn
	ON cct.CountryCode = ccn.Code
WHERE ccn.Code = "BIM"
GROUP BY ccn.Code
;

DROP TABLE copy_city;
DROP TABLE copy_country;
