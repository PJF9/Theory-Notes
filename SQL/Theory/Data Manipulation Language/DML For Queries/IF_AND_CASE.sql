-- There are two different functions categories:
--   1) Functions that acts only on a certain type of data
--   2) Functions that does not depend on the data types

-- The first general function that we are going to see is `IF`
-- Syntax: IF(test_expr, true_val, false_val)
-- Which is simply saying that if the `test_expr` is true it is going to return the `true_val`,
-- 	 otherwise the `false_val`
-- Can be used in all clauses, but most common we are going to use it inside `SELECT`
-- Database: classicmodels
SELECT IF(o.status = "Shipped", "Shipped", "Not Shipped") AS status, COUNT(*) AS orders
FROM orders o
GROUP BY 1
;

-- Another function is `IFNULL` that if the first expresion return a `NULL` value it is going to
-- 	 be replaced by the second expression
-- Syntax: IFNULL(test_expr, null_expr)
-- Notice that by IF we can build IFNULL: IF(test_expr IS NULL, null_expr, test_expr)

-- Another function is `NULLIF` that if the 2 expressions are equal returns NULL, otherwise
-- 	 it returns the expression
-- Syntax: NULLIF(expr1 = expr2)
-- From IF: IF(expr1 = expr2, NULL, expr1)
SELECT c.customerName, IFNULL(CONCAT(e.firstName, " ", e.lastName), "None") AS companyEmployee
FROM customers c LEFT JOIN employees e
	ON c.salesRepEmployeeNumber = e.employeeNumber
ORDER BY 2
;


-- Another function is `CASE`
-- Syntax: CASE expression
-- 		   		WHEN expr1 THEN res1
-- 				[WHEN expr2 THEN res2]
-- 				...
--              [ELSE default]
--         END AS alias
-- Meaning that if the expression has the value of expr1 it will select res1, if not
-- 	 then it will continues to the next `WHEN` and go on until find some expri
-- If non of the expression match the original, it is going to select the default value
SELECT 
	CASE p.productLine
		WHEN "Classic Cars" THEN "Cars"
        WHEN "Vintage Cars" THEN "Cars"
        WHEN "Trucks and Buses"  THEN "Cars"
        ELSE p.productLine
	END AS productLine , COUNT(*) AS products
FROM productlines p
GROUP BY 1
;

-- Another syntax for `CASE` is:
SELECT 
	CASE
		WHEN o.orderDate >= "2003-01-01"
			AND o.orderDate <= "2003-12-31" THEN "2003"
		WHEN o.orderDate >= "2004-01-01"
			AND o.orderDate <= "2004-12-31" THEN "2004"
		ELSE "Other"
	END AS orderData, COUNT(*) AS orders
FROM orders o
GROUP BY 1
;

-- At last we also have `COALESCE` (kοαλές) which is returning the first from the expressions
--   that is not NULL
-- Syntax: COALESCE (expr1 [, expr2 [, ...]])






