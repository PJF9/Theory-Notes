-- Database classicmodels

-- Syntax: WHERE operand OP operand
-- As an operand we can use either a column or a literal value
-- A literal can be a number, a string or either a time format ("YYYY-MM-DD HH:MM:SS")
-- As an operator (OP) we can use any comparisson operator (Note not-equal is defined as '<>'), or a combination of those

-- Select only the records that has `quantityInStock` bigger than the literal 9000
SELECT productName, quantityInStock
FROM products
WHERE quantityInStock >= 9000
;

-- Note that the column at `WHERE` doesn't need to be selected
SELECT productCode, productName, productLine
FROM products
WHERE productVendor = "Welly Diecast Productions"
;

-- How we think about creating a query?
-- First we think about the table(s), thus `FROM`, then the filter: `WHERE` and at last the display: `SELECT`

-- An example using time format
SELECT *
FROM orders
WHERE orderDate > "2005-05-16"
;

-- We can combine logical expressiong using `NOT`, `AND`, `OR` (NOT > AND > OR)
SELECT *
FROM employees
WHERE NOT jobTitle = "Sales Rep"
;
SELECT *
FROM products
WHERE (productLine = "Motorcycles") AND (productVendor = "Highway 66 Mini Classics")
;
SELECT *
FROM products
WHERE (productLine = "Classic Cars") OR (productLine = "Motocycles")
ORDER BY productLine, quantityInStock DESC
;
SELECT *
FROM orders
WHERE (orderDate = "2004-04-13") OR 
	  (orderDate >= "2004-05-01" AND orderDate <= "2004-05-31")
;

-- In order to save time each time we want to write `column >= low_value AND column <= high_value` we can use the clause `BETWEEN`
-- Those values can be any literal we want
-- Syntax: column BETWEEN low_value AND high_value
SELECT *
FROM orderdetails
WHERE priceEach BETWEEN 100 AND 200
;

-- Instead of writing a lot of `OR`s we can use the clause `IN` (We can also use `NOT IN`, that performs the oposite of `IN`)
-- Syntax: column IN (value1, value2, ...)
SELECT productName, productLine, productVendor
FROM products
WHERE productLine IN ("Motorcycles", "Classic Cars")
ORDER BY productLine DESC
;
SELECT *
FROM offices
WHERE country NOT IN ("USA", "Australia")
;

-- We can discard records with `NULL` values using `IS NOT NULL`
-- Thats because `column = NULL` and `column <> NULL` are always false
-- Note that the result of any operation include NULL in NULL
-- To check for NULL we use `IS` clause
SELECT *
FROM country
WHERE IndepYear IS NULL
;
SELECT *
FROM country
WHERE IndepYear IS NOT NULL
;
-- Note that NULL values dont appear in the query bellow
SELECT *
FROM country
WHERE IndepYear <> 1919
;















