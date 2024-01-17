-- Displays the top 3 of cities temperature during July and August--desc.
SELECT city, temperature
FROM temperature
WHERE month IN ('July', 'August')
ORDER BY temperature DESC
LIMIT 3;
