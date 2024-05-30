-- In real world applications a programming language is connected to the DBMS and allow us to take
-- 	 data and modify eazily the database.
-- Often we want to exract some information multiple times, or let's say insert multiple records or
--   even insert on mulpiple tabels.
-- By now the only way to do those tasks is by each time writting the same query. To avoid writting
--   the same code again and again MySQL supports `STORED PROCEDURES`, that are the equivalant of
--   function in ordenary high level programming languages. The return of the procedure has to be a
--   result set (a `SELECT` statement). The last select statement is the return value.

-- Syntax: DELIMITER $
--         CREATE PROCEDURE proc_name()
--         BEGIN 
--             ...
--         END $$
--         DELIMITER ;

-- The `DELIMITER $$` replace the `;`, and allow us to create a procedure with multiple lines and be
--   able to use queries inside of the procedure.
-- Note that '$$' can be anything that is not part of MySQL alphabet

-- To call a procedure  : CALL proc_name();
-- To delete a procedure: DROP [IF EXISTS] proc_name;
-- MySQL does not supports a way to update a procedure, so we need to delete it and create it again.

DELIMITER &&
CREATE PROCEDURE hallo_world()
BEGIN
	SELECT "Hallo World" AS first_message;
END &&
DELIMITER ;    

CALL hallo_world();
DROP PROCEDURE hallo_world;












