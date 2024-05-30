SELECT contactFirstName AS firstName, contactLastName AS lastName
FROM customers
;

SELECT CONCAT(contactFirstName, " ", contactLastName) AS contactPerson
FROM customers
;

SELECT DISTINCT country AS countries
FROM customers
;

SELECT MIN(creditLimit) AS minCredits,
	   MAX(creditLimit) AS maxCredits,
	   AVG(creditLimit) AS avgCredits
FROM customers
;
