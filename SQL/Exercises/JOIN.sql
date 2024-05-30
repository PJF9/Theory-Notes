-- Database: world
SELECT cn.Name AS Name, cl.Language AS Language, cl.Percentage AS Percentage
FROM countrylanguage cl JOIN country cn
	ON cl.CountryCode = cn.Code
;

-- Database: classicmodels
SELECT pd.productName AS name, pl.productLine AS productLine, pd.quantityInStock AS quantityInStock
FROM products pd JOIN productlines pl
	ON pd.productLine = pl.productLine
;

SELECT c.customerName AS customer, c.city AS city,
       SUM(p.amount) AS total_amount, c.creditLimit AS credit_limit
FROM payments p JOIN customers c
	ON p.customerNumber = c.customerNumber
WHERE c.country IN ("USA", "France")
GROUP BY c.customerNumber
ORDER BY c.creditLimit DESC
;

-- Database: sakila
SELECT l.name, COUNT(*) AS films
FROM film f JOIN language l
	ON f.language_id = l.language_id
GROUP BY f.language_id
;

SELECT CONCAT(ac.first_name, " ", ac.last_name) AS full_name, COUNT(fi.film_id) AS total_films
FROM film_actor fa
	JOIN film fi ON fa.film_id = fi.film_id
    JOIN actor ac ON fa.actor_id = ac.actor_id
GROUP BY ac.actor_id
ORDER BY total_films DESC
;
-- The same query can be written
SELECT CONCAT(ac.first_name, " ", ac.last_name) AS full_name, COUNT(fa.film_id) AS total_films
FROM film_actor fa JOIN actor ac 
	ON fa.actor_id = ac.actor_id
GROUP BY ac.actor_id
ORDER BY total_films DESC
;

SELECT f.title AS movie
FROM film_category fc
	JOIN category c ON fc.category_id = c.category_id
    JOIN film f ON fc.film_id = f.film_id
WHERE f.rating NOT IN ("R", "NC-17") AND 
	  f.length BETWEEN 60 AND 90 AND
      f.description REGEXP "boring|love|documentary" AND
      f.replacement_cost <= 14.00 AND
      c.name IN ("Travel", "Family", "Comedy", "Classics")
;

SELECT DISTINCT c.name AS categories
FROM film_actor as fa
	JOIN film_category fc ON fa.film_id = fc.film_id
    JOIN actor a ON fa.actor_id = a.actor_id
    JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name = "JULIA" AND a.last_name = "FAWCETT"
;

-- Database: classicmodels
-- Top motorcycles salesperson
SELECT CONCAT(e.firstName, " ", e.lastName) AS full_name, e.email, SUM(od.priceEach * od.quantityOrdered) as sold
FROM customers c
	JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    JOIN orders o ON c.customerNumber = o.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
    JOIN products p ON od.productCode = p.productCode
WHERE p.productLine = "Motorcycles"
GROUP BY e.employeeNumber
ORDER BY sold DESC
LIMIT 1
;

-- Databease: sakila
-- Movies we dont have at any store
SELECT f.title AS movie
FROM film f LEFT JOIN inventory i
	ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.title
;

SELECT f.title AS movie, COUNT(r.rental_id) AS total_rentals
FROM film f
	LEFT JOIN inventory i ON f.film_id = i.film_id
    LEFT JOIN rental r ON i.inventory_id = r.inventory_id
GROUP BY f.film_id
ORDER BY total_rentals DESC
;

-- Database: sakila
SELECT r.rental_id, r.rental_date, COUNT(p.payment_id) AS rentals, SUM(p.amount) AS amount
FROM rental r LEFT JOIN payment p
	ON r.rental_id = p.rental_id
GROUP BY r.rental_id
UNION
SELECT r.rental_id, r.rental_date, COUNT(p.payment_id) AS rentals, SUM(p.amount) AS amount
FROM rental r RIGHT JOIN payment p
	ON r.rental_id = p.rental_id
GROUP BY r.rental_id
;

-- Database: classicmodels
SELECT CONCAT(e2.firstName, " ", e2.lastName) AS manager, COUNT(e1.employeeNumber) AS total_employees
FROM employees e1 JOIN employees e2
	ON e1.reportsTo = e2.employeeNumber
GROUP BY e2.employeeNumber
ORDER BY total_employees
;

SELECT DISTINCT o.city
FROM employees e1 
	LEFT JOIN employees e2 ON e2.reportsTo = e1.employeeNumber
    JOIN offices o ON e1.officeCode = o.officeCode
GROUP BY e1.employeeNumber
HAVING COUNT(e2.employeeNumber) = 0
;

-- Database: sakila
SELECT CONCAT(c.first_name, " ", c.last_name) AS customer, SUM(p.amount) AS total_amount
FROM payment p JOIN customer c
	ON p.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_amount DESC
LIMIT 10
;

SELECT CONCAT(c.first_name, " ", c.last_name) AS customer, SUM(p.amount) AS total_amount
FROM customer c LEFT JOIN payment p
	ON c.customer_id = p.customer_id
GROUP BY c.customer_id
ORDER BY total_amount
LIMIT 100
;

SELECT cn.country, SUM(p.amount) AS total_amount
FROM country cn
	JOIN city ct ON cn.country_id = ct.country_id
    JOIN address a ON ct.city_id = a.city_id
    LEFT JOIN customer c ON a.address_id = c.address_id
    LEFT JOIN payment p ON c.customer_id = p.customer_id
GROUP BY cn.country_id
ORDER BY total_amount DESC
;









