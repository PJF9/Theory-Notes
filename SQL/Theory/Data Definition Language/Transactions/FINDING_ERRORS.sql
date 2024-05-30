-- When dealing with errors, MySQL gives us a way to spot exactly where the error occur
--   and the exacpt error message
-- The command: `SHOW ERRORS` gives us the information (error code and message) of the
--   last error that occur
-- To store those informations in variables we use the script:
-- 		GET DIAGNOSTICS CONDITION 1
--      	@var1 = MYSQL_ERRNO, @var2 = MESSAGE_TEXT;

-- (as obvious `MYSQL_ERRNO` gives us the error code and `MESSAGW_TEXT` the message)

DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	-- The variables to help us capture the errors
	DECLARE current_error VARCHAR(100);
    DECLARE error_string VARCHAR(300) DEFAULT "";
    DECLARE error_number INT;
    DECLARE error_message VARCHAR(50);
		
	-- Capturing the error into 'current_error'
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
		BEGIN
			GET DIAGNOSTICS CONDITION 1
				error_number = MYSQL_ERRNO, error_message = MESSAGE_TEXT;
            SET current_error = CONCAT(error_number, "-", error_message, " ");
		END;
	
    START TRANSACTION;
	
    -- First error handling
    SET current_error = "";
    INSERT INTO departments(dept_no, dept_name) 
		VALUES (4, "R&D");
    IF LENGTH(current_error) > 0 THEN
		SET error_string = CONCAT(error_string, "Q1:", current_error, " ");
	END IF;
    
	-- Second error hangling
    SET current_error = "";
    INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (2, "1970-01-01", "Justin", "Mac Alister", "M", "2018-01-01");
    IF LENGTH(current_error) > 0 THEN
		SET error_string = CONCAT(error_string, "Q2:", current_error, " ");
	END IF;
        
	-- Third error handling
    SET current_error = "";
	INSERT INTO dept_manager(dept_no, emp_no, from_date, to_date)
		VALUES (4, 2, "2019-01-01", "2021-01-01");
	IF LENGTH(current_error) > 0 THEN
		SET error_string = CONCAT(error_string, "Q3:", current_error, " ");
	END IF;
    
    -- The final condition to determine if we `COMMIT` or `ROLLBACK`
    IF LENGTH(error_string) > 0 THEN
		ROLLBACK;
        SELECT error_string AS message;
	ELSE
		COMMIT;
		SELECT "All good" AS message;
	END IF;
		
END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;
















