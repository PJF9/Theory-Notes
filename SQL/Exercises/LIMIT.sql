SELECT Name
FROM city
WHERE CountryCode = "GRC"
ORDER BY Population DESC
LIMIT 5
;

SELECT *
FROM countrylanguage
WHERE Language = "Greek"
ORDER BY Percentage DESC
LIMIT 2
;

SELECT *
FROM countrylanguage
WHERE Language = "Greek"
ORDER BY Percentage DESC
LIMIT 3, 5
;
