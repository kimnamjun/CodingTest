SELECT IF(SUBSTRING(datetime, 12, 1) = 0, SUBSTRING(datetime, 13, 1), SUBSTRING(datetime, 12, 2)) hour, COUNT(*)
FROM animal_outs
WHERE SUBSTRING(datetime, 12, 2) >= '09' AND SUBSTRING(datetime, 12, 2) < '20'
GROUP BY SUBSTRING(datetime, 12, 2)
ORDER BY SUBSTRING(datetime, 12, 2);