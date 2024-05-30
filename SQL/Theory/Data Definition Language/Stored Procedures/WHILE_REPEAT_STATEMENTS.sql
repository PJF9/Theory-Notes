-- MySQL support loops for giving us the access to control the flow of the procedure
-- Although it proviedes us `WHILE` and `DO WHILE` loop we have no `FOR` loop

-- Syntax: WHILE condition DO
--            statements
--         END WHILE;

-- Syntax: REPEAT
--            statements
--         UNTIL condition
--         END REPEAT;
-- (this is the do while loop)

-- Syntax: loop_name: LOOP
--            statements
--         END LOOP loop_name;
-- (this is an infinite loop that we can break using `LEAVE` and continue `ITERATE`)

-- A simple example to demonstrate loops
DELIMITER &&
CREATE PROCEDURE loops()
BEGIN
	DECLARE str1, str2, str3 VARCHAR(30) DEFAULT "";
    DECLARE i INT;
    
    SET i = 0;
    WHILE (i < 5) DO
		SET str1 = CONCAT(str1, " ", i);
        SET i = i + 1;
	END WHILE;
    
    SET i = 0;
    REPEAT
		SET str2 = CONCAT(str2, " ",  i);
        SET i = i + 1;
	UNTIL (i > 5)
    END REPEAT;
    
    SET i = 0;
    l: LOOP
		IF (i > 5) THEN
			LEAVE l;
		END IF;
        
		SET str3 = CONCAT(str3, " ", i);
        SET i = i + 1;
	END LOOP l;
        
    SELECT str1, str2, str3;
    
END &&
DELIMITER ;

CALL loops();
DROP PROCEDURE loops;
















