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

SELECT TOP 4 SaleID, CustomerName, TotalSale
FROM sales;

-- SaleID	CustomerName	TotalSale
-- 1	    Alice	        150
-- 2	    Bob	            200
-- 3	    Charlie	        300
-- 4	    David	        400

SELECT SaleID, CustomerName, TotalSale
FROM sales
LIMIT 4;
