-- MySQL supports if statements and case statements inside the procedures

-- Syntax: IF condition THEN
--         	  statements1
--         [ELSEIF condition2 THEN
--            statement2
--         ...
--         ]
--         [ELSE 
--            statementN
--         ]
--         END IF;

-- Syntax: CASE var THEN              |       CASE     
--            WHEN value1 THEN        |          WHEN condition1 THEN
--                statements1         |              statements1
--            [WHEN value2 THEN       |          [WHEN condition2 THEN
--                statements2         |              statements2
--            ...                     |          ...
--            ]                       |          ]
--            ELSE                    |          ELSE
--                statementsN         |              statementsN
--            END CASE;               |          END CASE;

-- (Note that the second `CASE` is the same as `IF`-`ELSEIF` statement)

-- Database: world
-- Let's say we want to find all the countries that are Independed from 1700 through 1900
DELIMITER &&
CREATE PROCEDURE indep()
BEGIN
	DECLARE from_year INT DEFAULT 1700;
    DECLARE total_years INT DEFAULT 100;
    
    IF (from_year + total_years > EXTRACT(YEAR FROM NOW())) THEN
		SELECT "Invalid Year Integral" AS error_message;
	ELSE
		SELECT Name, IndepYear
        FROM country
        WHERE IndepYear BETWEEN from_year AND from_year + total_years;
	END IF;
    
END &&
DELIMITER ;

CALL indep();
DROP PROCEDURE indep;



















