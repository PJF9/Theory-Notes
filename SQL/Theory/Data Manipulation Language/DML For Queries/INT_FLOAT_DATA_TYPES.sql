/*
	MySQL support those intager data types:
    1) TINYINT  : 1 byte  (-128 to 127)
    2) SMALLINT : 2 bytes (-32.768 to 32.767)
    3) MEDIUMINT: 3 bytes (-2^23 to -2^23 - 1, apr 8*10^6)
    4) INT      : 4 bytes (-2^31 to 2^31 - 1,  apr 2*1-^9)
    5) BIGINT   : 8 bytes (-2^63 to 2^63 - 1,  apr 9*10^18)
    
    MySQL support those floating data types:
    1) FLOAT : 4 bytes (1.4*10^-45 to 3.4*10^38)
    2) DOUBLE: 8 bytes (4.9*10^-324 to 1.8*10^308)
    
    We can also add `UNSIGNED` if we want unsigned numbers
    
    And for fixed poing floating numbers:
    1) DECIMAL(M, N): M the total digits and N the floating digits
		For example 3,14259 is a DECIMAL(6, 5)
        
	The functions that we can use to those data types are:
	1) ROUND(N[, L]) : Rounding to the Lth decimal digit (default is zero)
		If the Lth + 1 digit is smaller than five then the Lth digit remain the same,
		otherwise it will be increased by one.
    2) TRUNCATE(N, L): Cuts out from the Lth decimal digit
    3) CEILING(N)    : Returns the supremum intager of N
    4) FLOOR(N)      : Returns the infimum intager of N
    5) ABS(N)        : Returns the absolute value of N
    6) SIGN(N)       : Returns the sign of N
    7) POWER(N, P)   : Returns N^P
    8) RAND([SEED])  : Returns a random double from zero to one
*/

SELECT ROUND(1.23456), ROUND(1.23456, 1), ROUND(1.23456, 4);
SELECT TRUNCATE(1.23456, 0), TRUNCATE(1.23456, 1), TRUNCATE(1.23456, 2);
SELECT CEIL(1.234), FLOOR(1.234);
SELECT ABS(-9.1), SIGN(-9.1);
SELECT POWER(2,3) + 1;
SELECT RAND(), RAND(), RAND();












