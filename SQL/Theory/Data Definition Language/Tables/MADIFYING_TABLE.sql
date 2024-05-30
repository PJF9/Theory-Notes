-- MySQL supports adding, modifying and deleting a column from our table:
-- Syntax: ALTER table [database_name].table
-- 			  statement1,
-- 			  statement2,
-- 			  ...;
-- Where as statements we can use:
-- Syntax: ADD column_name data_type [atributes] [FIRST|AFTER col]
--         	 (`FIRST` means the new column is going to be placed at the start, and `AFTER` after col)
--         DROP COLUMN column_name
--         MODIFY column_name data_type [atributes] [FIRST|AFTER col]
-- On modification we need to take notice when changing the data type, otherwise we will get error

-- We can also modify the primary and the foreign keys of a table:
-- Syntax: ADD PRIMARY KEY (col1, col2)
-- 	       DROP PRIMARY KEY
-- For the foreign keys:
-- Syntax: ADD [CONSTRAINT [name]] FOREIGN KEY (col)
-- 		 		REFERENCES table(col) [ON DELETE CASCADE|SET NULL]
--  	   DROP FOREIGN KEY name
-- Note that we can not delete the primary key if it is also a foreign key

ALTER TABLE employees
	ADD email VARCHAR(100) NOT NULL AFTER last_name;
ALTER TABLE employees
	MODIFY email VARCHAR(50) NOT NULL FIRST;
ALTER TABLE employees
	MODIFY email VARCHAR(50) CHARSET "utf8mb4" COLLATE "utf8mb4_unicode_ci";
ALTER TABLE employees
	DROP COLUMN email;

ALTER TABLE salaries
	DROP FOREIGN KEY salaries_fk;
ALTER TABLE salaries
	DROP PRIMARY KEY;
ALTER TABLE salaries
	ADD PRIMARY KEY (emp_no, from_date);
ALTER TABLE salaries
	ADD CONSTRAINT salaries_fk_emp FOREIGN KEY (emp_no)
		REFERENCES employees(emp_no) ON DELETE CASCADE;

-- Another modification we can perform is to rename and delete all records
-- Syntax: RENAME TABLE old_table TO new_table
--         TRUNCATE TABLE table_name

CREATE TABLE actor AS
	SELECT *
    FROM classicmodels.offices;
RENAME TABLE actor TO offices;
DROP TABLE offices;

-- All these modifications can be done using the workbench









