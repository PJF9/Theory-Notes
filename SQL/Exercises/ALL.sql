-- DB: sakila

-- Get the number of movies an actor have play
SELECT CONCAT(first_name, " ", last_name) AS actor_name, COUNT(*) AS total_films
FROM film_actor fa
	JOIN actor a ON fa.actor_id = a.actor_id
    JOIN film f ON fa.film_id = f.film_id
GROUP BY a.actor_id
HAVING total_films > 30
ORDER BY total_films DESC
LIMIT 9
;

-- Customers who have rented more that 40 movies
SELECT CONCAT(first_name, " ", last_name) AS customer_name, COUNT(*) total_rents
FROM payment p JOIN customer c
	ON p.customer_id = c.customer_id
GROUP BY c.customer_id
HAVING total_rents >= 40
ORDER BY total_rents DESC
;


-- Database: classicmodels

-- Get total orders per vehicle category
SELECT COUNT(*) AS totalOrders,
	CASE p.productLine
		WHEN "Classic Cars" THEN "Ground Vehicle"
        WHEN "Vintage Cars" THEN "Ground Vehicle"
        WHEN "Trucks and Buses" THEN "Ground Vehicle"
        WHEN "Motorcycles" THEN "Ground Vehicle"
        WHEN "Trains" THEN "Ground Vehicle"
        WHEN "Ships" THEN "Sea Vehicle"
        WHEN "Planes" THEN "Air Vehicle"
		ELSE "Other" END
	AS vehicleType
FROM orders o
	JOIN orderdetails od ON o.orderNumber = od.orderNumber
	JOIN products p ON od.productCode = p.productCode
GROUP BY vehicleType
;

-- Get total amount a customer has paid
SELECT c.contactFirstName, c.contactLastName, SUM(pm.amount) as totalAmount
FROM customers c
	JOIN payments pm ON c.customerNumber = pm.customerNumber
    JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN offices oc ON e.officeCode = oc.officeCode
WHERE oc.country IN ("USA", "France")
GROUP BY c.customerNumber
;


-- The total amount of sales that have been sold from employees that their offices are in USA and France
SELECT oc.country, COUNT(*) AS totalSales, SUM(od.quantityOrdered * od.priceEach) AS totalAmount,
	CASE p.productLine
		WHEN "Classic Cars" THEN "Ground Vehicle"
        WHEN "Vintage Cars" THEN "Ground Vehicle"
        WHEN "Trucks and Buses" THEN "Ground Vehicle"
        WHEN "Motorcycles" THEN "Ground Vehicle"
        WHEN "Trains" THEN "Ground Vehicle"
        WHEN "Ships" THEN "Sea Vehicle"
        WHEN "Planes" THEN "Air Vehicle"
		ELSE "Other" END
	AS vehicleType
FROM customers c
	JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
	JOIN products p ON od.productCode = p.productCode
    JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN offices oc ON e.officeCode = oc.officeCode
WHERE oc.country IN ("USA", "France") AND o.status = "Shipped"
GROUP BY vehicleType, oc.country
ORDER BY totalAmount DESC
;


-- The same excercise using sub-queries
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
