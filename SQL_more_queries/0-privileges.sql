--  a script that lists all privileges of the MySQL users user_0d_1
-- and user_0d_2 on your server (in localhost).
SELECT *
FROM localhost
FULLOUTER JOIN user_0d_1 AND user_0d_2;
