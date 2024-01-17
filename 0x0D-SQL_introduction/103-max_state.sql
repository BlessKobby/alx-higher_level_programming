-- Displays the max temp of each state ordered by state name.
SELECT state, MAX(temperature) AS max_temperature
FROM temperatures
GROUP BY state
ORDER BY state
