-- Database: world

-- Syntax: SELECT * | [DISTINCT | ALL] column1 [AS alias1], column2 [AS alias2], ...

-- Selecting everything from `city` table of the `world` database
SELECT *
FROM city
;


-- Selecting only one column of this table, with alias
-- One key concept about SQL is that it's not case sensitive, meaning that `name` is the same as `NaMe`
SELECT name AS Country_Name
FROM city
;

-- Can also select more than one column
SELECT id, name, population AS Country_Population
FROM city
;

-- With the keyword `DISTINCT` we are selecting only the different records, of those we have selected
SELECT DISTINCT continent
FROM country
;

-- Note that with `DISTINCT` we can have records with same value at a column
SELECT DISTINCT name, continent
FROM country
;

-- With `ALL` is like selecting without any keyword
SELECT ALL continent
FROM country
;

-- When a column consists with cumputable data, such as string or number we can perform calculation to them
-- We see some `NULL` values, meaning the lack of information about that record
SELECT Name AS Country, (2020 - IndepYear) AS Years_Free
FROM country
;

-- To make calculation we also use (other than operators) functions
-- `CONCAT` is the function that concatinates two or more string
SELECT CONCAT(HeadOfState, " of ", name) AS Ruler, Continent
FROM country
;

-- Another function is `AVG` that selects the average value of a column
SELECT AVG(LifeExpectancy) AS Average_Life_Expectacy
FROM country
;

-- We can use the keyword `FROM` with two or more tables
-- The result will be the cartasian product of the records from the two or more tables
SELECT *
FROM city, country
;






