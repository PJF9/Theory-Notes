-- Database: sakila
-- Deleting Mary Smith from all database as a customer
CREATE TABLE copy_address AS SELECT * FROM address;
CREATE TABLE copy_city AS SELECT * FROM city;
CREATE TABLE copy_country AS SELECT * FROM country;
CREATE TABLE copy_customer AS SELECT * FROM customer;
CREATE TABLE copy_rental AS SELECT * FROM rental;
CREATE TABLE copy_payment AS SELECT * FROM payment;





-- HELPING QUERIES
-- Address id of Mary Smith
SELECT address_id
FROM copy_customer
WHERE first_name = "Mary" AND last_name = "Smith"
;
-- City Id of Mary Smith
SELECT city_id
FROM address
WHERE address_id = (
	SELECT address_id
	FROM copy_customer
	WHERE first_name = "Mary" AND last_name = "Smith"
	)
;
-- Country id of Mary Smith
SELECT country_id
FROM copy_city
WHERE city_id = (
	SELECT city_id
    FROM address
    WHERE address_id = (
		SELECT address_id
		FROM copy_customer
		WHERE first_name = "Mary" AND last_name = "Smith"
		)
	)
;
SELECT COUNT(*) - 1 AS customers_with_the_same_address_as_Mery_Smith
FROM customer c
WHERE c.address_id = (
	SELECT address_id
	FROM copy_customer
	WHERE first_name = "Mary" AND last_name = "Smith"
    )
;
SELECT COUNT(*) - 1 AS customers_with_the_same_city_as_Mery_Smith
FROM customer c
	JOIN address a ON c.address_id = a.address_id
WHERE a.city_id = (
	SELECT city_id
	FROM address
	WHERE address_id = (
		SELECT address_id
		FROM copy_customer
		WHERE first_name = "Mary" AND last_name = "Smith"
		)
	)
;
SELECT COUNT(*) - 1 AS customers_with_the_same_country_as_Mery_Smith
FROM customer c
	JOIN address a ON c.address_id = a.address_id
    JOIN city ct ON a.city_id = ct.city_id
WHERE ct.country_id = (
	SELECT country_id
	FROM copy_city
	WHERE city_id = (
		SELECT city_id
		FROM address
		WHERE address_id = (
			SELECT address_id
			FROM copy_customer
			WHERE first_name = "Mary" AND last_name = "Smith"
			)
		)
	)
;
--  END OF HELPING QUERIES





-- Delete country of Mary Smith if has no other customers
DELETE FROM copy_country
WHERE country_id = (
	SELECT country_id
	FROM copy_city
	WHERE city_id = (
		SELECT city_id
		FROM address
		WHERE address_id = (
			SELECT address_id
			FROM copy_customer
			WHERE first_name = "Mary" AND last_name = "Smith"
			)
		)
    ) AND (
		SELECT COUNT(*) - 1 AS customers_with_the_same_country_as_Mery_Smith
		FROM customer c
			JOIN address a ON c.address_id = a.address_id
			JOIN city ct ON a.city_id = ct.city_id
		WHERE ct.country_id = (
			SELECT country_id
			FROM copy_city
			WHERE city_id = (
				SELECT city_id
				FROM address
				WHERE address_id = (
					SELECT address_id
					FROM copy_customer
					WHERE first_name = "Mary" AND last_name = "Smith"
					)
				)
			)
		) = 0
;

-- Delete city of Mary Smith if it has no other customers
DELETE FROM copy_city
WHERE city_id = (
	SELECT city_id
	FROM address
	WHERE address_id = (
		SELECT address_id
		FROM copy_customer
		WHERE first_name = "Mary" AND last_name = "Smith"
		)
	) AND (
		SELECT COUNT(*) - 1 AS customers_with_the_same_city_as_Mery_Smith
		FROM customer c
			JOIN address a ON c.address_id = a.address_id
		WHERE a.city_id = (
			SELECT city_id
			FROM address
			WHERE address_id = (
				SELECT address_id
				FROM copy_customer
				WHERE first_name = "Mary" AND last_name = "Smith"
				)
			)
		) = 0
;

-- Delete address if only Mary Smith has this address
DELETE FROM copy_address
WHERE address_id = (
	SELECT address_id
	FROM copy_customer
	WHERE first_name = "Mary" AND last_name = "Smith"
	) AND (
		SELECT COUNT(*) - 1 AS customers_with_the_same_address_as_Mery_Smith
		FROM customer c
		WHERE c.address_id = (
			SELECT address_id
			FROM copy_customer
			WHERE first_name = "Mary" AND last_name = "Smith"
			)
		) = 0
;

-- Deleting all rentals of Mary Smith
DELETE FROM copy_rental
WHERE customer_id = (
	SELECT customer_id
    FROM customer
    WHERE first_name = "Mary" AND last_name = "Smith"
	)
;

-- Deleting all payments of Mary Smith
DELETE FROM copy_payment
WHERE customer_id = (
	SELECT customer_id
    FROM customer
    WHERE first_name = "Mary" AND last_name = "Smith"
	)
;

-- Finally deleting Mary Smith from customers
DELETE FROM copy_customer
WHERE customer_id = (
	SELECT customer_id
    FROM customer
    WHERE first_name = "Mary" AND last_name = "Smith"
	)
;


DROP TABLE copy_address;
DROP TABLE copy_city;
DROP TABLE copy_country;
DROP TABLE copy_customer;
DROP TABLE copy_rental;
DROP TABLE copy_payment;



















