-- Cursors gives that the option to iterate over a result set and read record after
--   record
-- We can use cursors inside stored procedures with the syntax:
-- DECLARE cursor_name CURSOR FOR query
-- (where as query we can have any query we want)

-- To collect the data and start the iteration we have to start the cursor:
--   OPEN cursor_name;
-- And after we are done we need to close it: CLOSE cursor_name

-- Then inside a loop we need to write: FETCH cursor_name INTO var1, var2, ...
-- To collect into vari the data from each record of column i
-- This line of code actually also moves the cursor to the next record

-- When the cursor reaches the end of result set, MySQL throws `NOT FOUND` error
--   so we can handle to break from the loop

-- We need to notice that cursors cna only be used for reading data not modifying
--   and the cursor can only move one way, can never go to a record that have already
--   fetch.

-- Let's see a procedure that calculates the total population of earth
DELIMITER &&
CREATE PROCEDURE total_population()
BEGIN
	DECLARE pop INT;
	DECLARE total_pop BIGINT DEFAULT 0;    
    DECLARE end_of_set INT DEFAULT 0;
	DECLARE pop_cursor CURSOR FOR
		SELECT Population
        FROM country
        WHERE Population IS NOT NULL;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND
		SET end_of_set = 1;
        
	OPEN pop_cursor;
			
    REPEAT
		FETCH pop_cursor INTO pop;
        SET total_pop = total_pop + pop;
    UNTIL end_of_set = 1
    END REPEAT;
    
    CLOSE pop_cursor;
    
    SELECT total_pop AS Population;

END &&
DELIMITER ;

CALL total_population();
DROP PROCEDURE IF EXISTS total_population;










