-- Works just like `LIKE`, but has more capabilities
-- Syntax: WHERE string_column [NOT] LIKE pattern
-- Those capabilities are:
-- 		'^str': starts with str
--      'str': contains str
--      'str$': ends with str
--      '^.s': second letter s (like '_' in `LIKE` clause)
--      'c*': contains c chatacter as many times we want (including zero)
--      'c+': contains c character as many times we want(with no zero)
--      'c?': contains c max one time
--      'c{n}': contains c exactly n times
--      'c{n,}': contains c at least n times
--      'c{n, m}': contains c at least n times and max m
--      '[abc]': contains either a, or b, or c
--      '[^abc]': is not containing a, b and c
--      '[0-9]': contains one number in the range zero to nine (likewise [^0-9])
--      '[a-z]': contains a character from a to z (likewise [^a-z]) (not case sensitive)
--      'str1|str2': either str1 or else str2
--      '\\.': contains '.'
--      '\\\': contains '\' ('\\special_char')

-- Class characters
-- Syntax: WHERE string_column REGEXP "...[[:class:]]..."
-- Provides us more options with ranges
-- 		alnum: alphanumeric characters
--  	alpha: alphabetic characters
--      blank: Whitespace characters
--      digit: Digit characters
--      lower/upper: lower/upper case characters

SELECT *
FROM city
WHERE Name REGEXP "^Par"
;

SELECT *
FROM city
WHERE Name REGEXP "ari"
;
SELECT *
FROM city
WHERE Name REGEXP "is$"
;
SELECT *
FROM city
WHERE (Name REGEXP "^.a") AND (Population > 2000000)
;

-- Contains 'b' and 'e' with that order and between them are three characters
SELECT *
FROM city
WHERE Name REGEXP "b...e"
;
-- Contains three characters
SELECT *
FROM city
WHERE Name REGEXP "^...$"
;
-- Contains max four characters
SELECT *
FROM city
WHERE Name NOT REGEXP "....."
;

-- Starts with 'b', contains 'e', and ends with 'a'
SELECT *
FROM city
WHERE Name REGEXP "^b.*e.*a$"
;
-- Contains substring that start with 'ab' and ends with 'ab'
SELECT *
FROM city
WHERE Name REGEXP "ab.*ab"
;
-- With '()' we can make thinks easier
SELECT *
FROM city
WHERE Name REGEXP "((ab).*){2}" -- ab.*ab.*
;
-- String with length multiple of three
SELECT *
FROM city
WHERE Name REGEXP "^(.{3})*$"
;

-- Starts with 'L' or 'M' and containing only characters
SELECT *
FROM city
WHERE Name REGEXP "^[^A-KN-Z][a-z]+$" -- double range
;

-- Cities that not containing only alphabetic characters
SELECT *
FROM city
WHERE Name NOT REGEXP "^[[:alpha:]]+$"
;


