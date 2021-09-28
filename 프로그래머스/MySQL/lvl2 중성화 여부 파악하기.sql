SELECT animal_id, name, IF(sex_upon_intake LIKE 'Intact%', 'X', 'O')
FROM animal_ins
ORDER BY animal_id;