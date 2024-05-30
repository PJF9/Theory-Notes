-- Database: world

-- Syntax: LIMIT [offset, ] rows
-- As offset we define the start of the 'limitation' and as rows the reocrds we want after the offset
-- The offset of the first records is zero, not one.

-- Selecting the first 9 records
SELECT *
FROM city
ORDER BY ID
LIMIT 9
;

-- Note we are selecting from ID 10 through 18
SELECT *
FROM city
ORDER BY ID
LIMIT 9, 9 
;