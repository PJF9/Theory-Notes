-- Database: city

-- Starts with 'b' and have length at least eight
SELECT *
FROM city
WHERE Name REGEXP "^b.{7}"
;

-- Contains three 'a's in a row
SELECT *
FROM city
WHERE Name REGEXP "a{3}"
;

-- Contains at least five 'a's
SELECT *
FROM city
WHERE Name REGEXP "(a.*){5}"
;

-- Starts with 'b', length at least eight and contains at least five 'a's and ends with 'r'
SELECT *
FROM city
WHERE Name REGEXP "^b.*(a.*){5}r$"
;


-- Database: classicmodels

-- Names starts with 'b' and containing either 'Co.' or 'Inc.' with or without the dot
SELECT *
FROM customers
WHERE customerName REGEXP "^B.*(Co(\\.?)|Inc(\\.?))"
;

-- Names starts with a vowel and has at least 7 chracters
SELECT *
FROM customers
WHERE contactLastName REGEXP "^[aeiouy].{6}"
;

-- Checking emails for validity
SELECT *
FROM employees
WHERE email NOT REGEXP "^[[:alpha:]]{2,}@[[:alpha:]]{3,}\\.com"
;

-- Last names with two consonants in a row and first names that start with 'L' and phones that contains 31 or 13
SELECT *
FROM employees
WHERE (firstName REGEXP "^L") AND (lastName REGEXP "[^aeiouy]{2}") AND (extension REGEXP "13|31")
;

SELECT customerNumber, SUM(amount) AS price
FROM payments
WHERE (checkNumber REGEXP "^[[:alpha:]]{2}[[:digit:]]{5}$")
GROUP BY customerNumber
HAVING price > 100000
ORDER BY price DESC
;

