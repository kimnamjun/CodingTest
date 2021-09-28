SELECT outs.animal_id, outs.name
FROM animal_ins ins RIGHT OUTER JOIN animal_outs outs ON ins.animal_id = outs.animal_id
WHERE ins.animal_id IS NULL
ORDER BY outs.animal_id;