-- Lists all the cities contained in the database hbtn_0d_usa
-- Can ONLY use one SELECT statement and the results must be sorted in ascending order by cities.id
-- Database name is passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON  state_id = states.id
ORDER BY cities.id;
