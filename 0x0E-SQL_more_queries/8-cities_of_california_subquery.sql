-- List all the cities of California found in the database
SELECT id, name FROM hbtn_0d_usa.cities WHERE hbtn_0d_usa.cities.state_id = (SELECT id FROM hbtn_0d_usa.states WHERE name = 'California') ORDER BY hbtn_0d_usa.cities.id;
