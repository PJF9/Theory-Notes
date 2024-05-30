-- For creating a database we use the syntax: CREATE DATABASE [IF NOT EXISTS] database_name;
-- If the database we want to create already exists then we will get an error

-- For deleting a database we can use: DROP DATABASE [IF EXISTS] database_name;
-- Again if the database doen not exists we will get an error

-- With the keyword `USE` we are telling MySQL that we work with this database
-- We can refer to tables of other databases as: other_database.table_name

CREATE DATABASE temp;
USE temp;

CREATE TABLE customers AS
	SELECT *
    FROM classicmodels.customers
;

SELECT * FROM customers;

DROP DATABASE temp;
