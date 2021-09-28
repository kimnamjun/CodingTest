-- MySQL
SELECT ins.name, ins.datetime
FROM animal_ins ins LEFT OUTER JOIN animal_outs outs ON ins.animal_id = outs.animal_id
WHERE outs.datetime IS NULL
ORDER BY ins.datetime
LIMIT 3;

-- Oracle
SELECT ins.name, ins.datetime
FROM animal_ins ins LEFT OUTER JOIN animal_outs outs ON ins.animal_id = outs.animal_id
WHERE outs.animal_id IS NULL
ORDER BY datetime
FETCH FIRST 3 ROW ONLY