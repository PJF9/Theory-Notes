-- `UNION` returns union of the results two, or more queries
-- Meaning that the records from the second query are placed after the ones from the first query
-- Each query must return the same number of columns and it is common used to be the same (not necessarily)
-- As column names MySQL picks the ones from the first query
-- We can't use `ORDER BY` at each query, we can only place it at the end (after the final query)
-- Syntax: QUERY-1
--         UNION [ALL]
--         QUERY-2
--         UNION [ALL]
--         ...
-- By the extension `ALL` if a record appeared both at the first and the second query, we are selecting it twice
-- (by default we are selecting it only once)

-- Database: world
SELECT c.Code, c.Name, c.Continent
FROM country c
WHERE c.Name REGEXP "^Ar"
UNION
SELECT c.Code, c.Name, c.Continent
FROM country c
WHERE c.Name REGEXP "ia$"
;

-- Database: classicmodels (select the customers and the employees)
SELECT c.customerName AS name, c.country, c.city, c.addressLine1 AS address
FROM customers c
UNION
SELECT CONCAT(e.firstName, " ", e.lastName), o.country, o.city, o.addressLine1
FROM employees e JOIN offices o
	ON e.officeCode = o.officeCode
ORDER BY name
;