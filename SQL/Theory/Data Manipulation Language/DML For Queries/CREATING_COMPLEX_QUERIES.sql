/*
	When we are asked to create a complex query:
		1) We break the problem into smaller problems
		2) We find the intermediate tables we need for the smaller problems
		    (and find the queries for their calculation)
		3) We proceed and starting building the query (first the smaller
		    problems and then the larger)

-- Example: classicmodels
/*
	We are asked to create a table that contains the total amount of sales 
    that have been sold from employees that their offices are in USA and
	Franch.
    As products we define `Ground/Air/Sea Vehicles`
*/


-- The bruteforce aproach, starting from head and going to bottom
SELECT off.country, 
	CASE p.productLine
		WHEN "Classic Cars" THEN "Ground Vehicle"
        WHEN "Vintage Cars" THEN "Ground Vehicle"
        WHEN "Trucks and Buses" THEN "Ground Vehicle"
        WHEN "Motorcycles" THEN "Ground Vehicle"
        WHEN "Trains" THEN "Ground Vehicle"
        WHEN "Ships" THEN "Sea Vehicle"
        WHEN "Planes" THEN "Air Vehicle"
		ELSE "Other"
	END AS vehicleType, SUM(od.quantityOrdered * od.priceEach) AS totalAmount
FROM employees e
	JOIN offices off ON e.officeCode = off.officeCode
	JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders o ON o.customerNumber = c.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
WHERE off.country IN ("USA", "France") AND o.status = "Shipped"
GROUP BY off.country, vehicleType
ORDER BY totalAmount DESC
;


-- First we are creating the vehicle types
SELECT 
	CASE p.productLine
		WHEN "Classic Cars" THEN "Ground Vehicle"
        WHEN "Vintage Cars" THEN "Ground Vehicle"
        WHEN "Trucks and Buses" THEN "Ground Vehicle"
        WHEN "Motorcycles" THEN "Ground Vehicle"
        WHEN "Trains" THEN "Ground Vehicle"
        WHEN "Ships" THEN "Sea Vehicle"
        WHEN "Planes" THEN "Air Vehicle"
		ELSE "Other"
	END AS vehicleType
FROM productlines p
;

-- Only orders and joining to get shipped orders
SELECT *
FROM orders o
	JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
WHERE o.status = "Shipped"
;

-- Combining those two queries and getting the fields we might need
SELECT o.orderNumber, o.customerNumber, (od.quantityOrdered * od.priceEach) AS price,
	CASE p.productLine
		WHEN "Classic Cars" THEN "Ground Vehicle"
        WHEN "Vintage Cars" THEN "Ground Vehicle"
        WHEN "Trucks and Buses" THEN "Ground Vehicle"
        WHEN "Motorcycles" THEN "Ground Vehicle"
        WHEN "Trains" THEN "Ground Vehicle"
        WHEN "Ships" THEN "Sea Vehicle"
        WHEN "Planes" THEN "Air Vehicle"
		ELSE "Other"
	END AS vehicleType
FROM orders o
	JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
WHERE o.status = "Shipped"
;

-- Next its time for offices
SELECT c.customerNumber, o.country
FROM customers c
	JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN offices o ON e.officeCode = o.officeCode
WHERE o.country IN ("USA", "France")
;

-- After that we are ready to combine them all
SELECT country, vehicleType, SUM(price) AS totalAmount
FROM (
	SELECT o.orderNumber, o.customerNumber, (od.quantityOrdered * od.priceEach) AS price,
		CASE p.productLine
			WHEN "Classic Cars" THEN "Ground Vehicle"
			WHEN "Vintage Cars" THEN "Ground Vehicle"
			WHEN "Trucks and Buses" THEN "Ground Vehicle"
			WHEN "Motorcycles" THEN "Ground Vehicle"
			WHEN "Trains" THEN "Ground Vehicle"
			WHEN "Ships" THEN "Sea Vehicle"
			WHEN "Planes" THEN "Air Vehicle"
			ELSE "Other"
		END AS vehicleType
	FROM orders o
		JOIN orderdetails od ON o.orderNumber = od.orderNumber
		JOIN products p ON od.productCode = p.productCode
	WHERE o.status = "Shipped"
	) AS ovt
    JOIN (
		SELECT c.customerNumber, o.country
		FROM customers c
			JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
			JOIN offices o ON e.officeCode = o.officeCode
		WHERE o.country IN ("USA", "France")
        ) AS ov
		ON ovt.customerNumber = ov.customerNumber
GROUP BY country, vehicleType
ORDER BY totalAmount DESC
;




