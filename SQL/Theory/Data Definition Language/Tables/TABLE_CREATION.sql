-- For creating table along side `AS` and `LIKE` we use:
-- CREATE TABLE [datadase_name.]table_name
-- 	(
--    column_1 datatype1 [atributes1] [,
-- 	  column_2 datatype2 [atributes2] [,
-- 	  ...]]
--  );
-- Where column_i is the name of the i-field, datatypei the data type of i-filed
-- 	 and attributes, as many as we want from:
--   NOT NULL, UNIQUE, AUTO_INCREMENT, DEFAULT default_value
-- The attributes are seperated using spaces

-- Although we can create tables using the workbench
-- 1) Right click on Table (in a database) and then `Create Table`
-- 2) Pass the name of the table
-- 3) We fill the boxes and press enter to insert the other columns we want to have
-- 4) Press aply and we are ready

-- Now its time to talk about 'primary keys'
-- MySQL provides us twp way to add a primary key to our tables:
-- 1) As the first atribute of a column: `PRIMARY KEY`
-- 2) Using `CONSTRAINT`: [CONSTRAINT [name]] PRIMARY KEY (col1, col2, ...)
-- Notice that we can pass a name for the constraint, most offen we name it 'table_pk'
-- 	 and also we can define two or more field as primary keys
-- The first way called 'column level' and the second  'table level'

-- With semilar way we can define `foreign keys`
-- We can also use both 'column level' and 'table level'
-- 1) col dtype [atributes] REFERENCES table(col) [ON DELETE CASCADE|SET NULL]
-- 2) [CONSTRAINT [name]] FOREIGN KEY (col)
-- 					REFERENCES table(col) [NO DELETE CASCADE|SET NULL]
-- That means: col is the foreing key of our table that links with 'col' from 'table'
-- `CASCADE` means that if the primary key deleted then the records of our table that
-- 	 has this value as foreing key will also get deleted.
-- Likewise `SET NULL`, will set as NULL the values of these fields.
-- We name the `CONSTRAINT` as: outTable_fk_table

-- MySQL provides us with `CONSTRAINT`s on the values of the records we want to add to
-- 	 the table. We can again use 'table' and 'column level'
-- Syntax: [CONSTRAINT [name]] CHECK (condition)
-- Where 'condition' can include as many fields we want. If a record don't passes the condition
-- 	 an error will occur.

-- In general we are going to use 'table level' when creating primary and foreing keys

-- Another think we can do is to create a field that used one or more other column. This is called
-- 	 'generated columns'
-- Syntax: column dtype ... AS (definition)
-- An example is: full_name VARCHAR(80) AS (CONCAT(first_name, ' ', last_name))
-- But it's a bad practice because using queries we can compute such result, make our database
-- 	 more complex.

-- MySQL gives us the option to encode strings with different ways. Each encoding breaks down to
-- 	 two parts: 'Character Set' and 'Collation'
-- 'Chracter Set' gives us all the characters we can use: example 'latin1' provides us all english
-- 	 character and 'utf8' inlude every character, greek, chinese, etc
-- 'Collation' is the way that those characters from 'Character Set' is classified. Two different
-- 	 'Collation's are '*__unicode_ci' that is a non case sensitive classification and '*__bin' that
-- 	 classifies the string according to the numbering of the encoding
-- We can define 'Character Set' and 'Collation' in three levels: 'Database', 'Table', 'Column'
-- Database: CREATE DATABASE [IF NOT EXISTS] name
-- 	         	CHARSET charset_name COLLATE collation_name;
-- Table:    CREATE TABLE name (
-- 		  		...
--           ) CHARSET charset_name COLLATE collation_name;
-- Column:   ...
--           col_name ... CHARSET charset_name COLLATE collation_name,
--           ...
-- The best (so far) character set we can use is 'utf8mb4' with collation 'utf8mb4__0900_ai_ci', which
-- 	 also works for greek characters.
-- 'Charset' and 'COLLATE' can be inluded in `ALTER TABLE` commands.

-- The last think we are going to discuss it 'Storage Engines'
-- The default 'Storage Engine' is 'InnoDB', but there are others like 'MyISAM', 'MEMORY', 'CSV' and 12
-- 	 others
-- Lets dig into 'InnoDB'. It supports:
-- 	 Referential Integrity: Table creation that link each other via primary and foreign keys
--   MVCC (Multiversion Concurrency Control): Simultaneously a user can	make modifycation to the
--   	database and another user can read without any inconsistency taking place (like reading
-- 	    unfinished data). This can be perform because there are multiple versions of data with
--      consistency versions depending of every use.
-- 	 Transaction Isolation: Is a process that arises from MVCC and is responsible to seperate each
--   	action of the database a indepented object that can not overlap (cover) other action of 
--      another user (also called link to the database)
-- 	 ACID Principle:
--      Atomicity: If a certain action set failed then it's possible to undo all the changes that
--      	took place in the database
--      Concistency: When some action set make modification to the database, it goes to a new state
-- 	   	    with no incocistancies.
--      Isolation: Every action set can not overlap with other actions
--      Durability: When an action set executed succesfully the base will be succesfully updated and 
--      	stored to the disk
-- 'MyISAM': Similar engine with the different that each lock is perform at table and not column level,
-- 	 thus its being used for only reading to the database and searching in big texts (full text search).
-- 	 It does not support primary and foreing key correlation.
-- 'MEMORY': Storing the results into the disk for faster response time (files)
-- 'CSV': Stores the values into a comma seperated format (Excel)

-- Let's say we want a table to have MyISAM as storage engine
-- Syntax: CREATE TABLE name (
--         	  ...
--         ) ENGINE = MyISAM;

DROP DATABASE IF EXISTS emp;
CREATE DATABASE emp
	CHARSET "utf8mb4" COLLATE "utf8mb4_unicode_ci";
USE emp;

CREATE TABLE employees (
	emp_no 		INT 	PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    birth_date	DATE 	NOT NULL,
    first_name	VARCHAR(30)	NOT NULL,
    last_name	VARCHAR(30)	NOT NULL,
    gender		ENUM("M", "F") NOT NULL DEFAULT "M",
    hire_date	DATE 	NOT NULL,
    
    CONSTRAINT date_constraint CHECK (hire_date > birth_date),
    CONSTRAINT birth_constraint CHECK (birth_date BETWEEN "1955-01-01" AND "2005-01-01")
);

CREATE TABLE departments (
	dept_no		INT	PRIMARY KEY NOT NULL UNIQUE,
    dept_name	VARCHAR(40)	NOT NULL
);

CREATE TABLE dept_manager (
	dept_no 	CHAR(4) NOT NULL,
	emp_no 		INT NOT NULL,
	from_date 	DATE NOT NULL,
	to_date 	DATE NOT NULL,
    
    CONSTRAINT dept_manager_pk PRIMARY KEY (dept_no, emp_no),
    CONSTRAINT dept_manager_fk_emp FOREIGN KEY (emp_no) 
		REFERENCES employees(emp_no) ON DELETE CASCADE
);

CREATE TABLE dept_emp (
	emp_no		INT NOT NULL REFERENCES employees(emp_no) ON DELETE CASCADE,
	dept_no 	INT NOT NULL REFERENCES departments(dept_no) ON DELETE CASCADE,
	from_date 	DATE NOT NULL,
	to_date 	DATE NOT NULL,
    
    CONSTRAINT dept_emp_pk PRIMARY KEY (emp_no, dept_no)
);

CREATE TABLE salaries (
	emp_no 		INT NOT NULL,
    salary		INT NOT NULL,
    from_date	DATE NOT NULL,
    to_date 	DATE NOT NULL,
    
    CONSTRAINT salaries_pk PRIMARY KEY (emp_no, from_date),
    CONSTRAINT salaries_fk_emp FOREIGN KEY (emp_no)
		REFERENCES employees(emp_no) ON DELETE CASCADE
);



