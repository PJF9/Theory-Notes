-- Other than INNER JOIN we can use OUTER JOIN.
-- OUTER JOIN can be categorised into 'left' and 'right'
-- This joining method works like INNER with the different that the selected table contains all the records
-- 	of the left (when using LEFT OUTER JOIN) or the right (when using RIGHT OUTER JOIN) that does not satisfy
--  the join condition declaring as NULL the field that are selected from the other table.
-- We are not going to use RIGHT JOIN, because it has the same functionality as LEFT

-- Most times we are using OUTER JOIN wo match primary and foreign keys for two (or more) tables
-- When the table with the foreign key is left, then if a foreign key does not got a match at right table
--   then this record will selected with NULLs to the fields of the reight table.
-- When the table with the foreign key is right, then if the primary key of the left table does not get any
--   match at the table with the foreign key, this record will be selected with NULLs at the fields of the
--   foreign key table.

-- Using both LEFT and RIGHT JOIN we can create the so called 'gull OUTER JOIN'
-- To do that we use the keyword `UNION` that applies on two tables that have the exact same fields
--   and selects them into one new table (records will not be addes twice)

-- Syntax: FROM table1 LEFT/RIGHT [OUTER] JOIN table2 ON join_condition
-- Where joing condition can be any logical expression between the columns of the two tables


-- Selecting the countries and the total cities they have
-- (With INNER JOIN we have no way to select those countries that have not any cities)
SELECT cn.Name AS country, COUNT(ct.CountryCode) AS cities
FROM country cn LEFT JOIN city ct
	ON ct.CountryCode = cn.Code
GROUP BY cn.Code
ORDER BY cities, country
;

-- Database: classicmodels
-- Selects the customer with the selesperson (some customer have not bought)
SELECT c.customerName AS customer, CONCAT(e.firstName, " ", e.lastName) AS asigned_to
FROM customers c LEFT JOIN employees e
	ON c.salesRepEmployeeNumber = e.employeeNumber
ORDER BY asigned_to
;

SELECT c.customerName AS customer, CONCAT(e.firstName, " ", e.lastName) AS employee
FROM customers c LEFT JOIN employees e
	ON c.salesRepEmployeeNumber = e.employeeNumber
UNION
SELECT c.customerName AS customer, CONCAT(e.firstName, " ", e.lastName) AS employee
FROM customers c RIGHT JOIN employees e
	ON c.salesRepEmployeeNumber = e.employeeNumber
;





