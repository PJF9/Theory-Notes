-- Database: classicmodels
-- Products with prices from average to max value
SELECT p.productName, p.buyPrice
FROM products p
WHERE p.buyPrice BETWEEN (SELECT AVG(products.buyPrice) FROM products) AND 
					     (SELECT MAX(products.buyPrice) FROM products)
ORDER BY p.buyPrice DESC
;

-- Customers that have bought at least one expensive product
SELECT c.customerName
FROM orderdetails od
	JOIN orders o ON od.orderNumber = o.orderNumber
    JOIN customers c ON o.customerNumber = c.customerNumber
WHERE od.priceEach >= (SELECT AVG(orderdetails.priceEach) FROM orderdetails)
GROUP BY c.customerNumber
ORDER BY customerName
;

-- Database: world
-- Continents with cities less than China and India combined
SELECT cn.Continent, COUNT(ct.ID) AS cities
FROM country cn JOIN city ct
	ON cn.Code = ct.CountryCode
GROUP BY cn.Continent
HAVING cities < (
	SELECT COUNT(*)
    FROM country cn JOIN city ct
		ON cn.Code = ct.CountryCode
	WHERE cn.Name IN ("China", "India")
	)
ORDER BY cities DESC
;


