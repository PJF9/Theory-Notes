-- Those are `COUNT`: total records on a column (not NULLs), `SUM`, `MIN`, `MAX`, `AVG`
SELECT COUNT(IndepYear) as FreeCountries
FROM country
;

-- Selecting the total records of the table
SELECT COUNT(*)
FROM country
;

SELECT COUNT(DISTINCT GovernmentForm) AS TotalForms, AVG(Population) AS AvgPopulation,
	   MIN(LifeExpectancy) AS MinLifeExpectancy, MAX(LifeExpectancy) AS MaxLifeExpectancy
FROM country
;