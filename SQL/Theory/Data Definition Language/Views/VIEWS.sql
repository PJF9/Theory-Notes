-- A `VIEW` (also called as Virtual Table) is a stored query that behaves like
-- 	 an ordenary table.
-- Syntax: CREATE [OR REPLACE] VIEW view_name [col1, col2, ...] AS query
-- With `OR REPLACE` if the view we want to create exists, it will repace the old
-- 	 view. Also col1, col2, ... are the new alias for the columns we want to inlude
-- To delete a view we use: DROP VIEW view_name
-- After we define the view we can use it exactly like an ordenary table
-- We use views to give different access to each user. Using views we can hide ceratin
-- 	 field from ceratin users and also to simplify the queries. We shall not forget
--   that views are queries that being executes each time we type it's name, thus
--   the downside is it takes more time than an ordenary table to execute the same query

-- After modifying a view all the modyfication are going to be passed to the 'real' table.

-- There are two views categories: 'updatable' and 'non updatable' view
-- A view is named 'updatable' when at the definition we have not used:
-- 	 `DISTINCT`, `HAVING`, `GROUP BY`, `UNION` and aggregate functions
-- If a view is updatable then we can modify it using: UPDATE view SET ...
-- Otherwise is 'non updatable' and if we try to update it we get an error
-- Another option we have is `WITH CHECK OPTION`, that simply tells us that if
-- 	 we perform an update (on the updatable view) and some record end up not
--   included in the view (using `WHERE` statement) MySQL will throw an error.
-- Syntax: CREATE [OR REPLACE] VIEW view AS
--         SELECT ...
--         ...
--         WITH CHECK OPTION;
-- Otherwise it just not going to be inserted to the view.

-- Other than update in an updatable view we can also `INSERT` and `DELETE` records
-- When inserting data into the view the fields that does not inlcuded in the view must have default
-- 	 values. We can add data into the view with the inverse way, by adding data to each table that
--   is being used to create the view. So at the end all this data is going to be inluded also to
--   the view, beacuse views are not tables but queries!
-- The option: `WITH CHECK OPTION` means that all the new data that is going to be inserted
--   must be inluded also in the view

-- Database: world
-- A view that inludes each country with each capital and some other information
CREATE OR REPLACE VIEW country_vw AS
SELECT cn.Code, cn.Name, cn.Continent, cn.Code2, ct.Name AS Capital, 
	   ct.Population AS CapitalPopulation
FROM country cn JOIN city ct
	ON cn.Capital = ct.ID
;
SELECT Name, Capital
FROM country_vw
ORDER BY CapitalPopulation DESC
;
CREATE OR REPLACE VIEW country_languages AS
SELECT cvw.Name AS Country, COUNT(*) AS Languages
FROM country_vw cvw JOIN countrylanguage cl
	ON cvw.Code = cl.CountryCode
GROUP BY cvw.Code
ORDER BY 1
;

-- Deleting the views
DROP VIEW country_vw;
DROP VIEW country_languages;

-- Database: emp
CREATE VIEW dept_vw AS
SELECT dept_name
FROM departments
;
UPDATE dept_vw
SET dept_name = "New name"
WHERE dept_name = "Some name"
;
CREATE OR REPLACE VIEW non_updatable AS
SELECT dept_name, COUNT(*) AS total_depts
FROM departments
GROUP BY dept_name
;
UPDATE non_updatable
SET dept_name = "New name for ALL"
;
-- An example with `WITH CHECK OPTION`
CREATE OR REPLACE VIEW dept_vw AS
SELECT dept_no
FROM departments
WHERE dept_no < 4
WITH CHECK OPTION
;
-- The new dept_no can not live in the view
UPDATE dept_vw
SET dept_no = 9
WHERE dept_no = 1
;

-- Inserting and deleting in the view
ALTER TABLE departments
	MODIFY dept_name VARCHAR(40) NOT NULL DEFAULT "None";

CREATE OR REPLACE VIEW dept_vw AS
SELECT dept_no
FROM departments
WHERE dept_no < 3
WITH CHECK OPTION
;

INSERT INTO dept_vw
VALUES (1);
INSERT INTO dept_vw
VALUES (2);
INSERT INTO dept_vw
VALUES (3);

UPDATE departments
SET dept_no = 4
WHERE dept_no = 1
;

CREATE OR REPLACE VIEW dpt_manager AS
SELECT d.dept_name AS department, CONCAT(e.first_name, " ", e.last_name) AS manager
FROM dept_manager dm
	JOIN departments d ON dm.dept_no = d.dept_no
    JOIN employees e ON dm.emp_no = e.emp_no
WITH CHECK OPTION
;

INSERT INTO departments
VALUES (1, "Logistics");
INSERT INTO employees
VALUES (1, "1980-01-01", "Gandalf", "The Gray", "M", "1981-01-01");
INSERT INTO dept_manager
VALUES (1, 1, "1990-01-01", "1995-01-01");
    
SELECT * FROM dpt_manager;
    
-- Erase modification
ALTER TABLE departments
	MODIFY dept_name VARCHAR(40) NOT NULL;
DELETE FROM departments;
DELETE FROM employees;
DROP VIEW dept_vw;
DROP VIEW dpt_manager;
DROP VIEW non_updatable;












