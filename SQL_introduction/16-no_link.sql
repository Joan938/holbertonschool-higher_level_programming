SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
-- Path: SQL_introduction/16-no_link.sql