-- We are going to see how to select columns of more than one table. This process is called JOINS
-- There are two different type of joints: cross join and inner join
-- When the tables we are selecting have fields with the same names then we are distinct them using 'table1.columnX', 'table2.columnX', ...
-- Also we can create table aliases: 'FROM table1 t1, ...'

-- Cross joins helps us selecting the cartesian product of the tables we are choosing. It's not so powerfull
-- The most powerfull join method is Inner Join
-- It is based on 'primary' and 'foreign' keys (The essence of the Relational DBMS)
-- As primary key we define a column in our table that to each record it gives different values, meaning that if 'colum1' is a primary key
-- 	then 'SELECT DISTINCT COUNT(column1)' gives the number of the records in the data base. Usually as a primary key we define an ID, or a
-- 	code relavent to each record.
-- As a foreign key we define a column in our table that contains (as data) the primary keys of another table.

-- We are Joining the tables according to primary and foreign keys. Let's say we want to Join two tables t1 (primary + foreing Keys) and t2
-- 	(primary Keys). Then each record of the t1 looks to match it's foreign key to a record at the t2 table (it is ceratin that it's 1-1) and
-- 	when it finds it the two records becomes one and selected to go to the new table
-- It is clear that the joint table contains exactly as much records as the table that contains the primary and foreing keys.
-- If the foreign key has a NULL value then this record will not be selected on the joined table.

-- Which table we are choosing to go first when joining does not really matter. We choose to write first the table that contains
-- 	the foreign key.
-- Also as best practice we are always using table alias.

-- Syntax: FROM table1 [t1] CROSS JOIN table2 [t2] [CROSS JOIN table3 [t3] [...]]
-- 		   FROM table1 [t1] [INNER] JOIN table2 [t2] ON table1.fk = table2.pk
-- (where 'fk' is the primary foreign keys of table1 and 'pk' the primary keys of table2)

-- To JOIN more than two tables use use the syntax:
--         FROM table1 [t1] 
--  	   		[INNER] JOIN table2 [t2] ON table1.fk = table2.pk
-- 				[INNER] JOIN table3 [t3] ON join_condition
--              ...
-- Where join_condition: Condition between the fk of the joined table and the pk of table3
--                       Condition between a pk of the joined table and the fk of table3

-- If fk, pk has the same name then we can use the keyword `USING` as USING(pk) and its the same
-- 	 as the `ON` statement (note we dont pass table.column, we pass only column)

-- When using INNER JOIN we are not limited on using it with primary and foreign keys. We can use it for
-- 	any column we want. In fact we are not bounded on the equity condition either, we can use any
-- 	comparisson condition we want. That's because it works like CROSS JOIN with WHERE clause and if a record
-- 	passes the clause then its selected for the joined table.



SELECT cn.name AS Country, ct.name AS City
FROM country cn CROSS JOIN city ct
;
SELECT *
FROM city ct JOIN country cn
	ON ct.CountryCode = cn.Code
;
-- Database: classicmodels
SELECT CONCAT(e.firstName, " ", e.lastName) AS fullName, o.city AS city
FROM employees e JOIN offices o
	ON e.officeCode = o.officeCode
;
-- The same think with CROSS JOIN can be written
SELECT CONCAT(e.firstName, " ", e.lastName) AS fullName, o.city AS city
FROM employees e CROSS JOIN offices o
WHERE e.officeCode = o.officeCode
;
-- The same with USING statement
SELECT CONCAT(e.firstName, " ", e.lastName) AS fullName, o.city AS city
FROM employees e 
	JOIN offices o USING (officeCode)
;

-- Database: world
-- Selecting the langueage spoken and the population of the two biggest cities of Greece
SELECT ct.Name AS city, ct.Population AS population, COUNT(*) AS languages_spoken
FROM city ct 
	JOIN country cn ON ct.CountryCode = cn.Code
    JOIN countrylanguage cl ON cn.Code = cl.CountryCode
WHERE cn.Name = "Greece"
GROUP BY ct.Name, ct.Population
ORDER BY ct.Population DESC
LIMIT 2
;



