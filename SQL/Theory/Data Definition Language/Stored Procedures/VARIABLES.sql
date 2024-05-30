-- To declare a varaible inside a procedure we use: DECLARE var_name [DEFAULT value];
-- After that we can initialize it: SET var_name = expression
-- (where expression can be a constant, procedure return and even a `SUBQUERY`)

-- We can also initialize the variables using a `SELECT` statement:
-- 	 SELECT val1, val2, ... INTO var1, var2, ... FROM ...;
-- In that case: var1 = val1, var2 = val2, ...

-- Those variables are local variables with scope only inside `BEGIN`-`END`
-- Using the prefix '@' we can define global variables, that has to be decrared
--   outside of the procedure. Each user has its own global variables, meaning that
--   @x for user1 will be different from @x of user2.
-- Lastly we can define system variables, using the prefix '@@' that are global 
--   variables which are visible and the same for all users.

DELIMITER &&
CREATE PROCEDURE variable()
BEGIN
	DECLARE x INT;
    SET x = 9;
    SELECT x;
END &&
DELIMITER ;

CALL variable();
DROP PROCEDURE variable;


DELIMITER &&
CREATE PROCEDURE variable()
BEGIN
	SET @x = @x + 3;
    SELECT @x;
END &&
DELIMITER ;

SET @x = 3;
CALL variable();
CALL variable();
DROP PROCEDURE variable;


-- Database: world
-- A procedure that returns the country with the maximum and the country with the
--   minimum population
DELIMITER &&
CREATE PROCEDURE min_max()
BEGIN
	DECLARE max VARCHAR(30);
    DECLARE min VARCHAR(30);

	SELECT Name INTO max
    FROM country
    WHERE Population = (
		SELECT MAX(Population)
        FROM country
		)
    ;
    SELECT Name INTO min
    FROM country
    WHERE Population = (
		SELECT MIN(Population)
        FROM country
        WHERE Population > 0
		)
    ;

	SELECT max, min;
END &&
DELIMITER ;

CALL min_max();
DROP PROCEDURE min_max;

-- Now let's say we also wanted the Population of those countries
DELIMITER &&
CREATE PROCEDURE min_max()
BEGIN
	SELECT Name, Population
    FROM country
    WHERE Population = (
		SELECT MAX(Population)
        FROM country
		)
	    OR
          Population = (
		SELECT MIN(Population)
		FROM country
		WHERE Population > 0
		);

END &&
DELIMITER ;

CALL min_max();
DROP PROCEDURE min_max;




