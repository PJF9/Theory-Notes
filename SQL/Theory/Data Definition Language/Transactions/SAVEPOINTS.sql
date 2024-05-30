-- Let's say that if a user messes up with our database we don't want to undo
--   every modification we has done, only after form certain point forwards
-- This can be done using: SAVEPOINT savepoint_name
-- We rollback using: ROLLBACK TO SAVEPOINT savepoint_name

-- Savepoints are extreamly usefull on large and multifunctional procedures

DELIMITER &&
CREATE PROCEDURE test()
BEGIN
	DECLARE err INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION SET err = 1;
	
    START TRANSACTION;
    
    INSERT INTO employees(emp_no, birth_date, first_name, last_name, gender, hire_date)
		VALUES (4, "1980-01-01", "Marry", "Jane", "F", "2018-01-01"); 
        
	SAVEPOINT point1;
    
    INSERT INTO dept_manager(dept_no, emp_no, from_date, to_date)
		VALUES (1, 1, "2019-01-01", "2021-01-01");
        
	IF err = 1 THEN
		ROLLBACK TO SAVEPOINT point1;
        SELECT "Error" AS mesage;
	ELSE
		COMMIT;
        SELECT "Ok" AS message;
	END IF;
    
END &&
DELIMITER ;

CALL test();
DROP PROCEDURE IF EXISTS test;


-- Let's say we want to add an employee even if an error occur into salary
-- For the emp_no we could define a varaible and using SELECT .. INTO to initialize it
DELIMITER &&
CREATE PROCEDURE add_employee(
	IN first_name_param VARCHAR(40),
    IN last_name_param VARCHAR(40),
    IN gender_param ENUM("M", "F"),
    IN birth_date_param DATE,
    IN hire_date_param DATE,
    IN salary_param INT,
    IN from_date_param DATE,
    IN to_date_param DATE
)
BEGIN
	DECLARE err INT DEFAULT 0;
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
		SET err = 1;
    
    START TRANSACTION;
    
    INSERT INTO employees(birth_date, first_name, last_name, gender, hire_date)
		VALUES (birth_date_param, first_name_param, last_name_param, gender_param, hire_date_param);
	
    SAVEPOINT employee_add;
    
    INSERT INTO salaries(emp_no, salary, from_date, to_date)
		VALUES (
        (
			SELECT emp_no
            FROM employees
            WHERE first_name = first_name_param AND last_name = last_name_param
        ),
        salary_param,
        from_date_param,
        to_date_param
        );
	
    IF err = 1 THEN
		ROLLBACK TO SAVEPOINT employee_add;
        SELECT "Error" AS message;
	ELSE
		COMMIT;
		SELECT "Ok" AS message;
	END IF;
    
END &&
DELIMITER ;

CALL add_employee(
	"Peter",
    "Floratos",
    "M",
    "2003-01-09",
	"2023-02-05",
	100000,
    "2023-02-05",
    "2023-03-05"
);
DROP PROCEDURE IF EXISTS add_employee;

