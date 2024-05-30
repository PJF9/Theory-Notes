-- Database: world
-- Selecting the largest and the capital of each country
SELECT cn.Name AS country, ct.Name AS city, ct.Population, "Capital" AS description
FROM country cn LEFT JOIN city ct
	ON cn.Capital = ct.ID
UNION
SELECT cn.Name, ct.Name, ct.Population, "Largest City" AS description
FROM country cn LEFT JOIN city ct
	ON cn.Code = ct.CountryCode
WHERE ct.Population = (SELECT MAX(city.Population) FROM city WHERE city.CountryCode = cn.Code)
ORDER BY country, description
;

-- Database: classicmodels
SELECT o.orderNumber AS order_number, c.customerName AS customer_name,
       SUM(od.quantityOrdered * od.priceEach) AS total_amount, CONCAT("Shipped on ", o.shippedDate) AS description
FROM orderdetails od 
	JOIN orders o ON od.orderNumber = o.orderNumber
    JOIN customers c ON o.customerNumber = c.customerNumber
WHERE o.status = "Shipped"
GROUP BY od.orderNumber
UNION
SELECT o.orderNumber, c.customerName,
       SUM(od.quantityOrdered * od.priceEach), "Pending..."
FROM orderdetails od 
	JOIN orders o ON od.orderNumber = o.orderNumber
    JOIN customers c ON o.customerNumber = c.customerNumber
WHERE o.status <> "Shipped"
GROUP BY od.orderNumber
ORDER BY total_amount DESC
;











