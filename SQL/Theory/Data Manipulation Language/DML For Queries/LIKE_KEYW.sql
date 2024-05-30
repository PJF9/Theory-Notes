-- We can perform much more complex conditions applied to string using `LIKE` clauses
-- Syntax: WHERE string_column  [NOT] LIKE pattern
-- As pattern is a string that can include "wildcards"
-- The that can inlcude are: `_`: Match exactly one character, `%`: Match many characters (0, 1, ..., N)

SELECT *
FROM country
WHERE Code LIKE "GR_"
;

SELECT *
FROM country
WHERE Code NOT LIKE "__C"
;

-- If we want all the countries that starts with G
SELECT *
FROM country
WHERE Name LIKE "G%"
;
-- All the countries that ends with 'y'
SELECT *
FROM country
WHERE Name LIKE "%y"
;

SELECT COUNT(*)
FROM city
WHERE Name LIKE "_____"
;







