-- For adding a `HAVING` clause we need first a `GROUP BY` one
-- It filters all the groups that has been creating base on some condition
-- Syntax HAVING condition
-- Most times the condition 'acts' on some aggregate result of the group
-- But can also 'act' on any of the select columns

SELECT Continent, COUNT(*) AS Countries
FROM country
GROUP BY Continent
HAVING Countries > 40
;

SELECT Continent, AVG(Population) AS AveragePopulation, MAX(LifeExpectancy) AS MaxLifeExpectancy
FROM country
GROUP BY Continent
HAVING MaxLifeExpectancy > 40
;

SELECT Continent, COUNT(*) AS Countries, AVG(Population) AS AvgPopulation
FROM country
WHERE IndepYear IS NOT NULL
GROUP BY Continent
HAVING Countries > 20 AND MIN(SurfaceArea) > 10
ORDER BY Countries DESC
LIMIT 5
;