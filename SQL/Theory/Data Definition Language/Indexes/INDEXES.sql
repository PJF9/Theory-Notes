-- Let's say we have a query that returns all records that have a specific value in
-- 	 a field. By default MySQL will perform serial searchm that is very slow when we
--   are dealing with large data.
-- We can perform this search much much faster using indexes. When we define a column
-- 	 as index then MySQL will create a B-tree for this column. So when we are searching 
--   the records that have a certain value in the 'index' columns the search is going to
--   be very fast.
-- Although if a column is 'index' then when adding or deleting records the process time
--   is slower because after adding/deleting the B-tree will rearange itself.
-- So we only use indexes on column that is going to be often used in queries.
-- MySQL by default create indexes for columns with the atributes `PRIMARY KEY` and `UNIQUE`

-- Syntax: CREATE [UNIQUE] INDEX index_name
--         ON table_name(col1 [, col2...])
-- Most offen indexes are only one column, but if two or more columns are specified it means
-- 	 that first the values are going to be sorted according to the first column, next second, etc
-- `UNIQUE` is an alternative way to define that the values of the column are unique
-- THe name of the index usually has this format: table_column_idx

-- To delete an index we use: DROP INDEX index_name

CREATE INDEX employees_last_name_idx
ON employees(last_name);

CREATE INDEX departments_dept_name_idx
ON departments(dept_name);

DROP INDEX employees_last_name_idx ON employees;
DROP INDEX departments_dept_name_idx ON departments;








