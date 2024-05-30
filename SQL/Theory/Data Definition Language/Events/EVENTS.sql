-- Events are blocks of code that execute in certain (and if we want) repetable
--   time intervals
-- Syntax: CREATE EVENT event
--         ON SCHEDULE AT timestamp
--         DO
--         	  BEGIN
--            ...
-- (this event will run the code on timestamp one time)

-- If we want to keep executing we can use:
-- CREATE EVENT event
-- ON SCHEDULE EVERY n interval [STARTS timestamp] [ENDS timestamp]  ...
-- (where n interval is n MINUTE, SECOND, HOUR, DAY, MONTH, YEAR)

-- As timestamp is a moment in time, but we can also use date

-- MySQL by default have disable events so to enable them we use:
-- SET GLOBAL event_scheduler = ON;
-- (and to OFF when we are done)

-- To see all the events that are running we use: SHOW EVENTS;
-- And to delete an event: DROP EVENT [IF EXISTS] event;


-- A good example is to delete the data from the audit, for GTPR
SET GLOBAL event_scheduler = ON;

SHOW EVENTS;

DELIMITER &&
CREATE EVENT delete_from_audit
ON SCHEDULE EVERY 1 MINUTE STARTS NOW()
DO
	BEGIN
		DELETE FROM employees_audit;
    END &&
DELIMITER ;

SELECT * FROM employees_audit;

DROP EVENT IF EXISTS delete_from_audit;
SET GLOBAL event_scheduler = OFF;









