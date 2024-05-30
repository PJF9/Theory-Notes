-- A transaction is a set of SQL commands that are going to be executed at the same
--   time into the server, by one user
-- Transactions can be a part either of SQL script or of stored procedures
-- Transactions are very usefull because most of the times more than one user will be
--   connected to our databases and lets say the first user starts inserting into the
--   tables and the seconds deletes some data that are crucial to the first user, the
--   a integrity problem have occur. With transactions we can deal with those kind
--   of problems. They simply work like: 'Do everythink, otherwise do nothing'
-- As discused, transactions are very usefull when inserting, updating and deleting data
--   from tables.

-- Syntax: START TRANSACTION;
--         ...
-- 	       COMMIT;

-- Some general advices regarding transactions:
-- 1) They have to de sort and perform only one job
-- 2) They have to not be opened for a long time
-- 3) `SELECT` statements should not be inlcuded into them
-- 4) Every time consuming action should be perfomed in times
--      that the database has little to zero user actions

DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	START TRANSACTION;
	
    INSERT INTO departments(dept_no, dept_name) 
		VALUES (1, "IT");
	INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (1, "1970-01-01", "Tywin", "Lannister", "M", "2020-01-01");
	INSERT INTO dept_manager(dept_no, emp_no, from_date, to_date)
		VALUES (1, 1, "2020-01-01", "2021-01-01");

	COMMIT;
END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;

-- Lets say a user decided to enter an employee with id 1
-- For now we will get an error but the new department will be add.
DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	START TRANSACTION;
	
    INSERT INTO departments(dept_no, dept_name)
		VALUES (2, "Marketing");
	INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (1, "1973-01-01", "Stephen", "Smith", "M", "2015-01-01");
	INSERT INTO dept_manager(dept_no, emp_no, from_date, to_date)
		VALUES (2, 2, "2016-01-01", "2021-01-01");
    
    COMMIT;
END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;












