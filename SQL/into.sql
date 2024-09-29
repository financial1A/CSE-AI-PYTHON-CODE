--Sales table
-- SaleID	CustomerName	TotalSale
-- 1	    Alice	        150
-- 2	    Bob	            200
-- 3	    Charlie	        300
-- 4	    David	        400
-- 5	    Eve	            250
-- 6	    Frank	        500
-- 7	    Grace	        100
-- 8	    Henry	        350
-- NULL	    NULL	        NULL

INSERT INTO top_sales (SaleID, CustomerName, TotalSale)
SELECT SaleID, CustomerName, TotalSale
FROM sales
ORDER BY TotalSale DESC
LIMIT 4;  -- For MySQL/PostgreSQL, or use TOP 4 for SQL Server


SELECT SaleID, CustomerName, TotalSale
INTO OUTFILE '/path/to/top_sales.csv'
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
FROM sales
ORDER BY TotalSale DESC
LIMIT 4;
