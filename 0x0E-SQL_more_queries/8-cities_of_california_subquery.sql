-- List all the cities of California found in the database
SELECT id, name FROM hbtn_0d_usa.cities WHERE hbtn_0d_usa.cities.state_id = (SELECT hbtn_0d_usa.states.id WHERE name = 'California');
