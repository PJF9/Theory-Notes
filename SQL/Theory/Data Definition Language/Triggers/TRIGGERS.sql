-- Triggers are block of codes (like procedures) that are executed every time after
--   an INSERT, DELETE or UPDATE
-- Syntax: CREATE TRIGGER trigger_name
--         AFTER|BEFORE INSERT|UPDATE|DELETE ON table
--         FOR EACH ROW
-- 		   	  BEGIN
--            ...

-- AFTER|BEFORE: When the trigger will be executed, after the change of before
-- INSERT|DELETE|UPDATE: On what task the trigger is going to be executed
-- FOR EACH: Iterate over the records that are affected by the action

-- We can access the new records (after|before an insertion or update) using
--   NEW.column
-- And the old ones (after|before deletion or update) using: OLD.column

-- Triggers are very usefull because we can use tham to make all sort of conditions
--   and prevent some misbehaivor and also for "audits"
-- Audits are tables that keep track all the action that have been done into a table

-- Triggers called themselfs automaticly so we dont need a `CALL` statement, although 
--   when we dont need them we can delete them using: DROP TRIGGER [IF EXISTS] trigger_name


-- We will see an example using audits for inserting
CREATE TABLE employees_audit (
	user	VARCHAR(40),
    action 	VARCHAR(10),
    changes	VARCHAR(200),
    stamp 	TIMESTAMP
);

-- This trigger is going to stored into 'employees' table tab
DELIMITER &&
CREATE TRIGGER tr_employees_after_insert
AFTER INSERT ON employees
	FOR EACH ROW
		BEGIN
			DECLARE changes VARCHAR(200);
            
            SET changes = CONCAT(
				NEW.emp_no, ", ",
                NEW.birth_date, ", ",
                NEW.first_name, ", ",
                NEW.last_name, ", ",
                NEW.gender, ", ",
                NEW.hire_date
				);
                
			INSERT INTO employees_audit
				VALUES (CURRENT_USER(), "INSERT", changes, CURRENT_TIMESTAMP());

		END &&
DELIMITER ;

INSERT INTO employees(birth_date, first_name, last_name, gender, hire_date)
	VALUES ("1970-01-01", "Tywin", "Lannister", "M", "2020-01-01");

SELECT * FROM employees;
SELECT * FROM employees_audit;

DROP TABLE employees_audit;
DROP TRIGGER tr_employees_after_insert;
DELETE FROM employees;


