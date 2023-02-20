-- no name order
SELECT score, name, COUNT(*) AS number
FROM second_table
WHERE name <> ''
GROUP BY score, name
ORDER BY number DESC;
