SELECT * FROM employee_table;
+-------------+------------+------------+---------------+
| EMPLOYEE_ID | LAST_NAME  | FIRST_NAME | DEPARTMENT_ID |
|-------------+------------+------------+---------------|
|         101 | Montgomery | Pat        |             1 |
|         102 | Levine     | Terry      |             2 |
|         103 | Comstock   | Dana       |             2 |
+-------------+------------+------------+---------------+

SELECT * EXCLUDE (department_id, employee_id) FROM employee_table;
+------------+------------+
| LAST_NAME  | FIRST_NAME |
|------------+------------|
| Montgomery | Pat        |
| Levine     | Terry      |
| Comstock   | Dana       |


SELECT * ILIKE '%id%' FROM employee_table;
+-------------+---------------+
| EMPLOYEE_ID | DEPARTMENT_ID |
|-------------+---------------|
|         101 |             1 |
|         102 |             2 |
|         103 |             2 |


SELECT * RENAME department_id AS department FROM employee_table;
+-------------+------------+------------+------------+
| EMPLOYEE_ID | LAST_NAME  | FIRST_NAME | DEPARTMENT |
|-------------+------------+------------+------------|
|         101 | Montgomery | Pat        |          1 |
|         102 | Levine     | Terry      |          2 |
|         103 | Comstock   | Dana       |          2 |
+-------------+------------+------------+------------+



SELECT * REPLACE ('DEPT-' || department_id AS department_id) FROM employee_table;
+-------------+------------+------------+---------------+
| EMPLOYEE_ID | LAST_NAME  | FIRST_NAME | DEPARTMENT_ID |
|-------------+------------+------------+---------------|
|         101 | Montgomery | Pat        | DEPT-1        |
|         102 | Levine     | Terry      | DEPT-2        |
|         103 | Comstock   | Dana       | DEPT-2        |
+-------------+------------+------------+---------------+