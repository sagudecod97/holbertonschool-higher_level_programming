-- List all cities with id, name and state
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;
