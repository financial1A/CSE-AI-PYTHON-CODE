SELECT employee_ID, manager_ID, title
  FROM employees
    START WITH title = 'Chief Investment Officer'
    CONNECT BY
      manager_ID = PRIOR employee_id
  ORDER BY employee_ID;

+-------------+------------+----------------------------+
| EMPLOYEE_ID | MANAGER_ID | TITLE                      |
|-------------+------------+----------------------------|
|           1 |       NULL | Chief Investment Officer   |
|          10 |          1 | Portfolio Manager - Equity |
|          20 |          1 | Portfolio Manager - Fixed Income        
|         100 |         10 | Equity Analyst             |
|         101 |         10 | Junior Equity Analyst      |
|         200 |         20 | Fixed Income Analyst       |
+-------------+------------+----------------------------+