-- A subquery is an SQL query inside of another query
-- To define a subquery we open parenthesis '()' and we write the subquery inside it
-- Those parenthesis could be placed at `SELECT`, `FROM`, `WHERE`, `HAVING`
-- The subquery depending on which clause we are using it, need to return either a value (using aggregate functions)
-- 	 either a column or a table.
-- We call the subquery as 'inner' query and the original query: 'outer'
-- The inner query have access to the tables of the outer query.
-- When a subquery correlate the tables of the inner and outer query it is called 'correlated subquery'
-- We can also have non-correlated subqueries.

-- The quastion that arises is: What to use JOIN or SUBQUERIES?
-- In most case it is much simpler (and faster by MySQL) to use JOIN.
-- But in the cases that we want to split the query into smaller ones or we want an aggregate
--    function in the query, we are going to use SUBQUERIES


-- When using subquery at the `SELECT` clause the subquery must return a single value
-- The same functionality (at the `SELECT` clause) can be achived using `JOIN` so generally we are not going to use
-- 	 is at `SELECT`
-- How it works: For every record that is selected to be at the finall table (or help calculate the single value) the
-- 	 subquery is executed and the result is stored at the finall table as a new field
-- We can have as many `SELECT subqueries' as we want
-- Syntax: SELECT col1, ..., (subquery) AS colk, ..., coln

SELECT CONCAT(c.contactFirstName, " ", c.contactLastName) AS fullName,
	   (
        SELECT SUM(p.amount)
        FROM payments p
        WHERE c.customerNumber = p.customerNumber
        GROUP BY c.customerNumber
       ) AS totalAmountPaid
FROM customers c
ORDER BY totalAmountPaid DESC
;
-- Non correlated subquery
SELECT CONCAT(c.contactFirstName, " ", c.contactLastName) AS fullName,
	   c.salesRepEmployeeNumber, c.creditLimit,
	   (
		SELECT AVG(p.amount)
		FROM payments p
       ) AS avgAmount
FROM customers c
;



-- When using subqueries inside a `FROM` clause the subquery can return both a value or a column and a table
-- The most common practice when using it inside `FROM` is to return a table
-- When we use subqueries to generate tables inside `FROM` first the subquery is executed and calculated and after
-- 	 that we can combine those tables with the 'regular typed' via joining methods
-- In correlation with before, we can have as many subqueries we want
-- Syntax: FROM t1, t2, ..., (subquery) tk, ..., tn

-- Selecting the amoung each customer paid and also the country, fullname etc (sakila)
SELECT ca.customer_name, ca.customer_country, ca.customer_city, ca.customer_address, SUM(p.amount) AS amount_paid
FROM payment p
JOIN (
	SELECT CONCAT(c.first_name, " ", c.last_name) AS customer_name, a.address AS customer_address,
		   ct.city AS customer_city, cn.country AS customer_country, c.customer_id
    FROM customer c
		JOIN address a ON c.address_id = a.address_id
        JOIN city ct ON a.city_id = ct.city_id
        JOIN country cn ON ct.country_id = cn.country_id
	 ) AS ca -- customer_address
		ON p.customer_id = ca.customer_id
GROUP BY ca.customer_id
ORDER BY amount_paid DESC
;
-- Return the avarage of maximum paids for each customer
SELECT AVG(max_customer_amount.max_amount) AS max_average_amount
FROM (
		SELECT MAX(p.amount) AS max_amount
        FROM customer c JOIN payment p
			ON c.customer_id = p.customer_id
		GROUP BY c.customer_id
    ) AS max_customer_amount
;



-- Using subqueries inside a `WHERE` clause is much more usefull than inside `SELECT` and `FROM`
-- The subquery must return either a value or a column, not a whole table
-- This method provide us a way to replace the 'values' inside the `WHERE` clause
-- (returns a value)
-- Syntax: WHERE operand OP operand (operand = column | (subquery))
-- 	       WHERE column BETWEEN low_value AND high_value (low_value/high_value = literal | (subquery)
-- (returns a column)
-- Syntax: WHERE column [NOT] IN (subquery)
-- 	       WHERE [NOT] EXISTS (subquery)

-- `EXISTS` is either true of false depending if any record have been selected or not
-- With `EXISTS` we are not interested what fields we selecting)
-- The same works perfectly with the `HAVING` clauses

-- Database: world
-- Selecting the countries that have population higher than the average population of earth
SELECT c.Name, c.Population
FROM country c
WHERE (c.Population > (SELECT AVG(country.Population) FROM country))
ORDER BY c.Population DESC
;
-- Selecting the countries with the maximum and the minimum population
SELECT c.Name, c.Region, c.Continent, c.Population
FROM country c
WHERE c.Population = (SELECT MAX(country.Population) FROM country) OR
	  c.Population = (SELECT MIN(country.Population) FROM country WHERE country.Population <> 0)
;

-- Database: classicmodels
-- Selects employees that reports to an employee on San Francisco
-- (can be written also with JOIN)
SELECT CONCAT(e.firstName, " ", e.lastName) AS name
FROM employees e
WHERE e.reportsTo IN (
	SELECT e.employeeNumber
    FROM employees e JOIN offices o
		ON e.officeCode = o.officeCode
    WHERE o.city = "San Francisco"
    )
;
-- Customers that have not taken any order
SELECT c.customerName
FROM customers c
WHERE NOT EXISTS (
	SELECT *
    FROM orders o
    WHERE o.customerNumber = c.customerNumber
	)
;




