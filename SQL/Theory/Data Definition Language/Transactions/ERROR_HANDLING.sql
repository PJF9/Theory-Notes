-- MySQL gives us options to handle with the exceptions that might occur when dealing
--   with the database.
-- In previous example we saw that if we tried to insert a record that has the same
--   primary key with another record we get an error, but all the changes done by that
--   user into the database prior to the wrong insertion will be commited

-- We can handle an error: DECLARE action HANDLER FOR condition statement (inside the BEGIN)
-- 'action'   : Either `EXIT` (not that usefull) or `CONTINUE` (to continue the procedure
--                instead of exiting.
-- 'condtion' : It can be either an error code (etc 1045 for access denied) or `SQLWARNING`
-- 	 	 	  	  to handle possible warnings, `SQLEXCEPTION` for ireversable error (etc the
-- 	 	 	      error with the wrong insertion), `NOTFOUND` (its about cursors and failure
--  	 	 	  in SELECT ... INTO statements) either `SQLSTATE` that couples all the above
-- 'statement': It can be either an SQL command (usually a SET statement for handling after) or
--  	 	      any other block of code that lives inside of a BEGIN/END statement
-- (we can note that the 'statement' is alwayse going to execute when an error will occur)

-- One way to deal with an error is to reverse the change that the 'failure' user causes to the
-- 	 database. This can be done using `ROLLBACK` instead of `COMMIT`

-- Lets say how to handle the wrong insertion
DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	DECLARE err INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET err = 1;
    
    START TRANSACTION;
    
    INSERT INTO departments(dept_no, dept_name) 
		VALUES (3, "Sales");
	INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (1, "1970-01-01", "Justin", "Mac Alister", "M", "2018-01-01");
	INSERT INTO dept_manager(dept_no, emp_no, from_date, to_date)
		VALUES (1, 1, "2019-01-01", "2021-01-01");
        
	IF err = 1 THEN
		ROLLBACK;
        SELECT "Error" AS error_message;
	ELSE
		COMMIT;
        SELECT "Ok" AS no_error_message;
	END IF;

END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;













