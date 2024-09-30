INSERT INTO my_table (id, name, value)
VALUES 
  (1, 'Alice', 100),
  (2, 'Bob', 200),
  (3, 'Charlie', 300);

-- Update Bob's value
UPDATE my_table SET value = 250 WHERE id = 2;

-- Delete Charlie's record
DELETE FROM my_table WHERE id = 3;

-- Insert a new record for Dave
INSERT INTO my_table (id, name, value) VALUES (4, 'Dave', 400);

SELECT *
FROM my_table CHANGES BETWEEN '2024-09-01 12:00:00' AND '2024-09-05 12:00:00';

ID	NAME	VALUE	CHANGE_TYPE	CHANGE_TIMESTAMP
2	Bob	    250	    UPDATE	    2024-09-03 14:00:00.000
3	Charlie	300	    DELETE	    2024-09-03 14:10:00.000
4	Dave	400	    INSERT	    2024-09-03 14:15:00.000