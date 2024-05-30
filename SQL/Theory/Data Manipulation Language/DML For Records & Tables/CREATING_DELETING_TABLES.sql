-- Modifying a database is considered bad practice, because we can't be one hundred percent
-- 	 sure that we are not going to fuck things up.
-- To prevent things for breaking we offen work either with a copy of our database or
-- 	 with at least copies of the tables we are modifying.
-- As soon as we are sure that all things work as expected then we update our database

-- For creating copies of a table we are using: CREATE TABLE new_table AS SELECT * FROM table
-- Creating a copy for each table in 'world' database
CREATE TABLE copy_city AS 
	SELECT *
    FROM city
;
CREATE TABLE copy_country AS
	SELECT *
    FROM country
;
CREATE TABLE copy_countrylanguage AS
	SELECT *
    FROM countrylanguage
;

-- For deleting a table MySQL supports: DROP TABLE table
DROP TABLE copy_city;
DROP TABLE copy_country;
DROP TABLE copy_countrylanguage;


-- Clicking on the screwdriver next to a table, a new window will pop up.
-- In the middle we have the stucture of the table
-- Column Name: The name of each field
-- Datatype: The datatype of each field
-- Then we have the attributes:
-- 	 PK: Primary Key
-- 	 NN: Not NULL, that means records can not have NULL values
--   UQ: Unique, only distinct values allowed
-- 	 UN, ZF: Deprecated
--   AI: Auto Increment
-- 	 G: Generated Column (field) 

















