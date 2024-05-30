/*
    For string MySQL supports:
    1) CHAR(N)              : For strings with length N (If a the length of a CHAR(N)
		string is less than N MySQL adds spaces)
	2) VARCHAR(N)           : For strings with length from zero to N (variable length)
    3) ENUM(s1, s2, ..., sn): With the values si an index is stored to faster access
    
    The functions that we can use for string data types are:
    1)  CONCAT(s1, ..., sn)       : The concatination of those n string
    2)  CONCAT_WS(d, s1, ..., sn) : The concatination of those n string with delimiter d
    3)  TRIM(s)                   : Removing all spaces from s
    4)  LTRIM(s)                  : The left trim of s
    5)  RTRIM(s)                  : The right trim of s
    6)  LENGTH(s)                 : The length of s
    7)  LEFT(s, n)                : The n-first characters of s
    8)  RIGHT(s, n)               : The n-last characters of s
    9)  SUBSTRING(s, START[, len]): A substring from s from index START until it has length len
    10) REPLACE(s, f, r)          : Replace f from s to r
    11) INSERT(s, start, len, s1) : Replace the substring from start to len into s1
    12) REVERSE(s)                : Reverses the string
    13) LOWER(s)                  : Casting into lower case the string
    13) UPPER(s)                  : Casting into upper case the string
    14) LPAD(s, l, p)             : Fills the s from left with p until s has length l
    15) RPAD(s, l, p)             : Fills the s from right with p until s has length l
    16) REPEAT(s, cnt)            : Repeat s cnt times
    17) SUBSTRING_INDEX(s, d, n)  : Splits the string into smaller string according to the delimiter d
		Returns the nth smaller string if n positive, otherwise the nth from the end
	18) LOCATE(f, s[, start])     : Returns the index of the first appearence of f inside f
		(start defines where to start searching)
*/

-- The field `Continent` from world::country is a ENUM data type
SELECT c.Continent, COUNT(*) AS Countries
FROM country c
WHERE c.Continent = "Asia" OR c.Continent = 2
GROUP BY c.Continent
;

-- Database: classicmodels
SELECT CONCAT(c.contactFirstName, " ", c.contactLastName) AS name
FROM customers c
ORDER BY LENGTH(name) DESC
LIMIT 1
;

SELECT 
	CASE SUBSTRING_INDEX(c.customerName, " ", -1)
		WHEN "Co." THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Co.", 1), ",", 1)
        WHEN "Co" THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Co", 1), ",", 1)
        WHEN "Ltd." THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Ltd.", 1), ",", 1)
        WHEN "Ltd" THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Ltd", 1), ",", 1)
        WHEN "Inc." THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Inc.", 1), ",", 1)
        WHEN "Inc" THEN SUBSTRING_INDEX(SUBSTRING_INDEX(c.customerName, "Inc", 1), ",", 1)
        ELSE customerName
	END AS customerName
FROM customers c
;

SELECT SUBSTRING(c.customerName, 1, LOCATE(" ", c.customerName) - 1) AS firstPart,
		SUBSTRING(c.customerName, LOCATE(" ", c.customerName)) AS firstPart, customerName
FROM customers c
;











