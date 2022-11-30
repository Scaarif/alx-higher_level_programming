-- Lists all the cities of Claifornia that can be found in the database hbtn_0d_usa
-- Not allowed to use the JOIN keyword
-- DO:
-- 	find out what the id of california is from states (a subquery)
-- 	THEN: get all cities whose state_id == california's id
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id;
