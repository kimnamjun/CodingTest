SELECT animal_type, COUNT(animal_type) count
FROM animal_ins
WHERE animal_type = 'Cat' OR animal_type = 'Dog'
GROUP BY animal_type
ORDER BY animal_type;