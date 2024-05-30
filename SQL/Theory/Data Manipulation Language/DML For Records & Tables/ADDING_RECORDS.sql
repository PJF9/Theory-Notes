-- For adding a record to a table we use: INSERT [INTO] table (col1, col2, ..., coln) VALUES (value1, value2, ..., valueN)
-- (to prevent the labor work: right-click to table, then 'Copy to Clipboard' and 'Insert Statement')
INSERT INTO copy_country
(`Code`, `Name`, `Continent`, `Region`, `SurfaceArea`, `IndepYear`, 
 `Population`, `LifeExpectancy`, `GNP`, `GNPOld`, `LocalName`,
  `GovernmentForm`, `HeadOfState`, `Capital`, `Code2`)
VALUES
("PJF", "Petropia", "Europe", "Cool Countries", 1.70, NULL,
 1, 83.5, 9000, 9000, "Cooltopia",
 "Top-G", "Me", NULL, "PJ");

-- We need to be careful which fields accept NULL as a value
-- There is an eazier way, by simply not writting the column names, but is effective for mistakes so we are
-- 	 going to skip it.

-- We can add more than one record, by seperating with comma the `VALUES` we want to add
INSERT INTO copy_country
(`Code`, `Name`, `Continent`, `Region`, `SurfaceArea`, `IndepYear`, 
 `Population`, `LifeExpectancy`, `GNP`, `GNPOld`, `LocalName`,
  `GovernmentForm`, `HeadOfState`, `Capital`, `Code2`)
VALUES
("PJG", "New Petropia", "Europe", "Cool Countries", 1.80, NULL,
 1, 83.5, 7000, 7000, "Cooltopia",
 "Top-G", "Me", NULL, "NP"),
 
 ("PJH", "Old Petropia", "Europe", "Cool Countries", 1.10, NULL,
 1, 83.5, 6000, 6000, "Cooltopia",
 "Top-G", "Me", NULL, "PJ");

-- By creating a table we asign default values to each field. So if we don't know for the
-- 	 the time being the values of some fields or we don't want to insert them we don't have
--   to. MySQL supports inserting records and asign values to at least one field
INSERT INTO copy_country (`Code`, `Name`)
VALUES ("PJI", "Petropia+");

INSERT INTO copy_country (`Code`, `Name`)
VALUES ("PFJ", "New Petropia+"),
	   ("PFF", "Old Petropia+");

-- Instead of passing each record manual we can add to a table the result of a query
-- Syntax: INSERT [INTO] table_name query
-- (The difference between `AS` and `LIKE`, is that `LIKE` does not add records)
CREATE TABLE favorite_countries LIKE copy_country;

INSERT INTO favorite_countries
SELECT *
FROM copy_country cc
WHERE cc.Code REGEXP "^PJ"
;

-- We can also specify which field we want each record to have value
-- (Be Careful: We need to SELECT only the fields we want to add)
INSERT INTO favorite_countries (`Code`, `Name`)
SELECT cc.Code, cc.Name
FROM copy_country cc
WHERE cc.Code REGEXP "^PF"
;
 
-- In general when we are trying to add to a table that one of its fields is the foreing
-- 	 key of another table, first we add the record to the table that contains the primary
-- 	 key and then to the table that contains the foreign key, because if we forget to
-- 	 add it to the primary key table then MySQL will throw an error. We are searching to
-- 	 find the first table and them move towards the table we want to add it.

-- Database: sakila
-- We want to add Joaquin Phoenix to actors that played to the film: Joker
-- First we need to see which fields are PK and which fields we want to add values
INSERT INTO actor (`first_name`, `last_name`)
VALUES ("JOAQUIN", "PHOENIX");
-- After that we need to add the film Joker (we go to find `language_id` from `language`)
INSERT INTO film (`title`, `language_id`)
VALUES ("Joker", 1);
-- Now is time to get actor and film id
SELECT actor_id
FROM actor
WHERE first_name = "JOAQUIN" AND last_name = "PHOENIX"
;
SELECT film_id
FROM film
WHERE title = "Joker"
;
-- actor_id = 201, film_id = 1001
 INSERT INTO film_actor (`actor_id`, `film_id`)
 VALUES (201, 1001);
 
 -- Printing the results
 SELECT f.title, CONCAT(a.first_name, " ", a.last_name) AS name
 FROM film_actor fa
	JOIN film f ON fa.film_id = f.film_id
    JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.title = "Joker"
;
 
 
 
 
 