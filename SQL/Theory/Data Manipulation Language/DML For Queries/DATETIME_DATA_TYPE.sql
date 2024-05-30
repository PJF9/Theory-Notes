/*
	For datetimes MySQL supports:
    1) DATE       : 3 bytes, format: yyyy-mm-dd (from 1.1.1000 to 31.12.9999)
    2) TIME       : 3 bytes, format: hh:mm:ss (from -838:59:59 to 838:59:59)
    3) DATETIME   : 8 bytes, format: yyyy-mm-dd hh:mm:ss (date from 1.1.1970 to 31.12.9999
		and time just like TIME)
	4) TIMESTAMP  : 4 bytes, format: yyyy-mm-dd hh:mm:ss (data from 1.1.1970 to 31.12.2037
		and time just like TIME)
	5) YEAR[(2|4)]: 1 byte , format yy | yyyy (from 1901 to 2155) and the format goes according
		to the argument (default is four)
	
    The format tells us how this inforamtion is stored in the database. With function we can
    change the way this information is displayed
    TIMESTAMP has a special purpose:
	- Defining field as TIMESTAMP, this column will automaticly update its values to the last
		point in time we affect and change the table
	
    Literal that we can use:
    1) DATE literals    : "yyyy-mm-dd" | "yyyy.mm.dd" | "yyyy/mm/dd" | "yyyymmdd" | yyyymmdd
    2) TIME literals    : "hh:mm:ss" | "hhmmss" | hhmmss
    3) DATETIME literals: first DATE and then TIME seperated with comma
    
    The functions that MySQL provide us are:
    1)  CURRENT_TIMESTAMP():
	    NOW()              : Returns the current date and time
	    SYSDATE()          :
	2)  CURRENT_DATE()     :
        CURDATE()          : Returns the current date
	3)  CURRENT_TIME()     :
        CURTIME()          : Returns the current time
	4)  UTC_DATE()         : Returns the UTC date
        UTC_TIME()         : Returns the UTC time
       
    5)  TIME_FORMAT(time, format): for modifying TIME data
    6)  DATE_FORMAT(date, format): for modifying DATE data
		 'format' is a string that contains some special cahracters
        
	7)  DAYOFMONTH(d): The day of the date d       (intager)
    8)  DAYOFWEEK(d) : The day of the week         (Sunday: 1, Monday: 2, ..)
    9)  DAYOFYEAR(d) : The day of the year         (intager)
    10) LAST_DAY(d)  : The last day of the month   (time)
    11) DAYNAME(d)   : The name of the day         (string)
    12) WEEK(d)      : The week of the year        (intager)
    13) MONTH(d)     : The month of the year       (intager)
    14) MONTHNAME(d) : The name of the month       (string)
    15) QUARTER(d)   : The half semester of year   (intager)
    16) YEAR(d)      : The year of the date        (intager)
    17) HOUR(d)      : The hour of the datetime    (intager)
    18) MINUTE(d)    : The minutes of the datetime (intager)
    19) SECOND(d)    : The seconds of the datetime (intager)
    
    We have another way of extracting data out of a datetime:
    21) EXTRACT(elem FROM data|time|datetime): Returns an intager that represents elem
    
    The last set of functions for dates and times:
    22) DATE_ADD(date, INTERVAL n elem): Adds to date n elem
    23) DATE_SUB(date, INTERVAL n elem): Subtract from date n elem
    24) DATEDIFF(date1, date2)         : The subtraction of date2 and date1
    25) TO_DAYS(date)                  : Total days from year 0
    26) TIME_TO_SEC(time)              : Returns the number of secods from midnight
    
    The formats we can use are:
	1) %s               : minutes (two digits, even zero)
    2) %i               : seconds (two digits, even zero)
    3) %H | %h          : hour (24th presentation | 12th presentasion)
    4) %p               : AM (before mid-day) | PM (after mid-day)
    5) %d | %e | %D | %a: day (01 | 1 | 1st | etc: Wed)
    6) %m | %c | %M | %b: month (01 | 1 | etc: January | etc: Jan)
	7) %y | %Y          : year (etc: 23 | etc: 2013 for 2023)
    8) %r               : hh:mm:ss (24th presentation)
    9) %T               : hh:mm:ss (12th presentation)
    
    The 'elem' we can use are:
    1)  SECOND
    2)  MINUTE
    3)  HOUR
    4)  DAY
    5)  MONTH
    6)  YEAR
    7)  MINUTE_SECOND: intager concatination from minute to seconds
    8)  HOUR_MINUTE  : intager concatination from hour to minute
    9)  DAY_HOUR     : intager concatination from day to hour
    10) YEAR_MONTH   : intager concatination from year to month
    11) HOUR_SECOND  : intager concatination from hour to second
    12) DAY_MINUTE   : intager concatination from day to minute
    13) DAY_SECOND   : intager concatination from day to second
*/

SELECT TIME_FORMAT("23:12:41", "Time: %h:%i:%s, %p");
SELECT DATE_FORMAT("2023-01-09", " My birthday was on: %a, %d/%M/%Y");

-- Orders each month of year
SELECT YEAR(o.orderDate) AS year, MONTHNAME(o.orderDate) AS month, COUNT(o.orderNumber) AS orders
FROM orders o
GROUP BY YEAR(o.orderDate), MONTHNAME(o.orderDate)
ORDER BY 1, MONTH(month)
;

SELECT o.orderNumber AS ordersLate
FROM orders o
WHERE DATE_SUB(o.shippedDate, INTERVAL 8 DAY) >= o.orderDate
;

SELECT o.orderNumber AS id, DATE_FORMAT(o.orderDate, "%d/%m/%Y") AS "order",
	   DATE_FORMAT(o.requiredDate, "%d/%m/%Y") AS "required",
       DATE_FORMAT(o.shippedDate, "%a, %D %M %Y") AS "shipped"
FROM orders o
;









