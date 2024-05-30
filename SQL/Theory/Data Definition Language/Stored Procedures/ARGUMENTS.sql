-- MySQL support argument parsing into the procedures.
-- We have three types of arguments: input (IN), output (OUT) and input/output (INOUT)
-- Syntax: CREATE PROCEDURE proc_name (
-- 	          [IN|OUT|INPUT] param1 datatype1,
-- 	          [IN|OUT|INPUT] param2 datatype2,
--            ...
--         )

-- Input variables are the defaults and also we cannot change them values.

-- Database: sakila
-- Geting the name and the movies of actor with id as parameter
DELIMITER &&
CREATE PROCEDURE actor(
	IN actor_id_param INT
)
BEGIN
	SELECT CONCAT(a.first_name, " ", a.last_name) AS fullname, COUNT(*) AS films
    FROM film_actor fa JOIN actor a
		ON fa.actor_id = a.actor_id
	WHERE a.actor_id = actor_id_param
    ;
END &&
DELIMITER ;

CALL actor(1);
DROP PROCEDURE actor;

-- Let's get this example using an output argument
DELIMITER &&
CREATE PROCEDURE actor(
	IN actor_id_param INT,
    OUT actor_name_param VARCHAR(30),
    OUT actor_movies_param INT
)
BEGIN
	SELECT CONCAT(a.first_name, " ", a.last_name), COUNT(*) 
		INTO actor_name_param, actor_movies_param
	FROM film_actor fa JOIN actor a
		ON fa.actor_id = a.actor_id
	WHERE a.actor_id = actor_id_param
    ;
END &&
DELIMITER ;

SET @name = "";
SET @movies = 0;
CALL actor(1, @name, @movies);
SELECT @name, @movies;
DROP PROCEDURE IF EXISTS actor;










