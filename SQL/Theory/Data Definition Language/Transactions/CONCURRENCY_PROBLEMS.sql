-- It's time to talk about concurency problems
-- We can solve those problem by simply locking the database for one user. The 
--   problem that occurs with that is when in our database a masive amount of
--   user login and making modifications and reading data. In order to partialy
--   solve this problem MySQL by default gives a timeout to each user.
-- So to actually solve this problem MySQL gives us the ability to disable some of
--   those concurency problems, via the so called `isolation levels`

-- First of all let's dig into the core concurency problems:
-- 1) Lost Updates       : When two or more users update the same record. Then by default
--                            the last update will conquer
-- 2) Dirty Reads        : When user A changes a record, user B reads that record and then
--                            user A rollbacks, then user B has data that doesn't exists
-- 3) Nonrepeatable Reads: When user A reads record R, user B changes record R and then
--                            user C read record R, then different user has different data
--                            from the same record
-- 4) Phantom Reads      : When user A updates a field from the table, user B insert a new
--                            record then user A at the end of its transaction has not update
--                            the entire table

-- The `ISOLATION LEVELS` that MySQL supports are:
-- 1) READ UNCOMMITED : Allows all concurency problems
-- 2) READ COMMITED   : Allows everything except `Dirty Reading`
-- 3) REPEATABLE READS: Allows only `Phantom Reads`
-- 4) SERIALIZABLE    : Prevents everything

-- (by default MySQL picks `REPEATABLE READS`)

-- The way to specify at the beginning of the transaction the isolation level is:
-- SET GLOBAL TRANSACTION ISOLATION LEVEL level
-- (where level, can be any of the above levels)

DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	DECLARE err INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
		SET err = 1;

	SET GLOBAL TRANSACTION ISOLATION LEVEL SERIALIZABLE;
    
    START TRANSACTION;
    
    INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (1, "2003-01-09", "Peter Jacob", "Floratos", "M", "2023-02-05");
        
	IF err = 1 THEN
		ROLLBACK;
        SELECT "Employee already exists..." AS message;
	ELSE
		COMMIT;
        SELECT "Added 1 employee to database..." AS message;
     END IF;
    
END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;



