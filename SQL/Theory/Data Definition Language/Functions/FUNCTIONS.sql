-- In our examples and exercises we have used functions, like aggregate functions, CONCAT(), etc
-- MySQL gives us the power to create our own functions
-- Syntax: DELIMITER &&
--         CREATE FUNCTION func_name(params) 
--         RETURN TYPE
--         STATEMENT
--         BEGIN
--            ...
--         	  RETURN value;
--         END &&
--         DELIMITER ;

-- As we see it's the same syntax like procedures with the difference that a function must always
--   return one value not a result set and as arguments we can only pass input parameters
-- As `STATEMENT` we can use at least one of:
--   1) DETERMINISTIC : produces the same output for every input
--   2) NO SQL        : does not include SQL command (queries)
--   3) READS SQL DATA: read (only) SQL data

-- We can call those functions as: func_name(param)
-- We can delete them: DROP FUNCTION func_name

DELIMITER &&
CREATE FUNCTION fact(n INT)
RETURNS INT
NO SQL
BEGIN
	DECLARE i INT DEFAULT 1;
    DECLARE res INT DEFAULT 1;
    WHILE (i<=n) DO
		SET res = res * i;
        SET i = i + 1;
	END WHILE;
    
    RETURN res;
END &&
DELIMITER ;

SELECT fact(5);
DROP FUNCTION fact;

-- An example that reads SQL data
DELIMITER &&
CREATE FUNCTION first_name(actor_id_param INT)
RETURNS VARCHAR(30)
READS SQL DATA
BEGIN
	DECLARE fname VARCHAR(30);
    
	SELECT first_name INTO fname
    FROM actor
    WHERE actor_id = actor_id_param
    ;
    RETURN fname;
END &&
DELIMITER ;

SELECT first_name(1);
DROP FUNCTION first_name;




















