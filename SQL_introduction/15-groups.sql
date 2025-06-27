SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
-- Path: SQL_introduction/15-groups.sql