SELECT CountryCode, COUNT(Name) AS Cities, SUM(Population) AS Population,
       AVG(Population) AS "Average Population"
FROM city
GROUP BY CountryCode WITH ROLLUP
;

SELECT Language, COUNT(*) Countries
FROM countrylanguage
GROUP BY Language
ORDER BY Countries DESC
;

SELECT GovernmentForm, COUNT(Code) AS Countries, MAX(GNP) AS "Max GNP",
       AVG(LifeExpectancy) AS "Average Life Expectancy",
       SUM(SurfaceArea) AS "Total Surface Area"
FROM country
GROUP BY GovernmentForm
ORDER BY GovernmentForm
;

SELECT GovernmentForm, COUNT(Code) AS Countries, MAX(GNP) AS "Max GNP",
       AVG(LifeExpectancy) AS "Average Life Expectancy",
       SUM(SurfaceArea) AS "Total Surface Area"
FROM country
WHERE Continent = "Europe"
GROUP BY GovernmentForm
ORDER BY GovernmentForm
;

SELECT city, COUNT(*) AS customers
FROM customers
WHERE country = "USA"
GROUP BY city
HAVING customers >= 2
ORDER BY customers DESC
;

SELECT productVendor, SUM(quantityInStock * buyPrice) AS totalPrice
FROM products
GROUP BY productVendor
HAVING totalPrice > 2500000
ORDER BY totalPrice DESC
;

SELECT state, COUNT(*) AS customers
FROM customers
WHERE state IS NOT NULL
GROUP BY state
ORDER BY customers DESC
;













