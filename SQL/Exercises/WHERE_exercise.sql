-- Database: classicmodels

SELECT customerName
FROM customers
WHERE contactFirstName = "Elizabeth"
;

SELECT customerName
FROM customers
WHERE creditLimit > 100000
;

SELECT CONCAT(firstName, " ", lastName) AS full_name
FROM employees
WHERE jobTitle <> "Sales Rep"
;

SELECT *
FROM payments
WHERE customerNumber = 398 AND 
	  (paymentDate >= "2004-01-01" AND paymentDate <= "2004-12-31")
;

SELECT *
FROM payments
WHERE (paymentDate >= "2004-01-01" AND paymentDate <= "2004-12-31")
  AND (amount >= 5000 AND amount <= 15000)
;

SELECT phone
FROM offices
WHERE city = "London" OR city = "Paris" OR city = "Tokyo"
;

SELECT CONCAT(addressLine1, " ", addressLine2, ", ", state, ", ", country) AS address
FROM offices
WHERE country = "USA"
;

SELECT customerName, country, creditLimit
FROM customers
WHERE (country = "Italy"
   OR country = "Spain"
   OR country = "USA")
  AND (creditLimit BETWEEN 100000 AND 120000)
ORDER BY country, creditLimit DESC
;

-- Database: world
SELECT Code
FROM country
WHERE Name IN ("Afghanistan", "Czech Republic", "Nigeria")
;

SELECT Name
FROM city
WHERE CountryCode IN ("AFG", "CZE", "NGA")
ORDER BY Name
;

SELECT DISTINCT GovernmentForm
FROM country
WHERE GovernmentForm NOT IN ("Republic", "Constitutional Monarchy")
ORDER BY GovernmentForm
;

SELECT Name AS Country, IndepYear as "Indepedence Year", 
       LifeExpectancy AS "Life Expectancy", Continent, 
       Population, SurfaceArea AS Surface
FROM country
WHERE (IndepYear IS NULL)
  AND (Continent IN ("Africa", "Asia"))
  AND (Population >= 100000)
  AND (SurfaceArea < 10000 OR SurfaceArea > 100000)
ORDER BY Population DESC
;

-- Database: classicmodels
SELECT SUM(quantityOrdered * priceEach) AS Price
FROM orderdetails
WHERE orderNumber BETWEEN 10100 AND 10199
;

SELECT productName
FROM products
WHERE productLine IN ("Vintage Cars", "Planes")
  AND productScale IN ("1:18", "1:32", "1:50")
LIMIT 5
;
  
SELECT city, phone, postalCode
FROM offices
WHERE (state IS NULL)
  AND (Country NOT IN ("USA", "France"))
;
  
  
  
  
  
  
  
  
  