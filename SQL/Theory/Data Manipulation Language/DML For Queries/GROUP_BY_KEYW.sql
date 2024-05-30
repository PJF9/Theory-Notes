-- This clause is written after `WHERE` clauses before `ORDER BY`
-- Using `GROUP BY` we are grouping records according to the values of a column that is selected
-- If a column is not selected then we can't group by this field
-- When grouping with two or more coulmns, each group is determined for all those columns
-- GROUP BY clauses are powerfull when combined with aggregate functions, because those function will applied to every group
-- Syntax: GROUP BY column1 [, column2 [, ... ]]

-- Selecting all the continents and the countries of each continent
SELECT Continent, COUNT(*) AS Countries
FROM country
GROUP BY Continent
;

-- Grouping with two columns
SELECT Continent, Region, COUNT(*) AS Countries
FROM country
GROUP BY Continent, Region
;

SELECT Continent, Region, COUNT(*) AS Countries
FROM country
WHERE Continent IN ("Europe", "Africa")
GROUP BY Continent, Region
ORDER BY Continent, Region DESC
LIMIT 30
;

-- With `ROLLUP` we are also selecting a record containing the total results of the aggregate function of the groups
-- Syntax: GROUP BY column1 [, column2 [, ... ]] [WITH ROLLUP]
SELECT Continent, Region, COUNT(*) AS Countries
FROM country
GROUP BY Continent, Region WITH ROLLUP
;