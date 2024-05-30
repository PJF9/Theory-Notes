-- Database: world

-- Syntax: ORDER BY expression [ASC | DESC] [, expression [ASC | DESC] [, ... ]
-- As expression we can use a column, a computable value (data) 
-- `ASC` stand for ascending (αυξουσα σειρα) and `DESC` for descending (φθινουσα σειρα)
-- By default `ORDER BY` sort the records in asceding order

SELECT *
FROM country
WHERE Region = "Caribbean"
ORDER BY name
;

-- Again we can order a column that is not selected
SELECT Name, Population
FROM country
WHERE Region = "Caribbean"
ORDER BY name DESC
;

-- We can order by more that one column
SELECT Name, Region
FROM country
ORDER BY Region, Name DESC
;

-- A lazy way that SQL provies us is reffer with number (1, 2, ...) the column that is selected and want to order by
SELECT CONCAT(HeadOfState, " of ", name) as Ruler, Population as Slaves
FROM country
ORDER BY 2 DESC
;

-- `NULL` values considered less than actual values
-- For actual values: special_chars < chars < numbers < letters

-- Exersise
SELECT Name, Continent, IndepYear
FROM country
WHERE GovernmentForm = "Republic"
ORDER BY Continent, IndepYear DESC
;
