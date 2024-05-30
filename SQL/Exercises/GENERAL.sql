-- Database: classicmodels
SELECT o.orderNumber, c.customerName, ROUND(SUM(od.quantityOrdered * od.priceEach)) AS amount
FROM orders o
	JOIN customers c ON o.customerNumber = c.customerNumber
    JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY o.orderNumber
ORDER BY 3 DESC
;

SELECT p.productName, p.quantityInStock, p.buyPrice,
	   ROUND(1.1*POWER(p.buyPrice, 1.1), 2) AS sellPrice, 
       ROUND((ROUND(1.1*POWER(p.buyPrice, 1.1), 2) - p.buyPrice) * p.quantityInStock, 2) AS profit
FROM products p
;