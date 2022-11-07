-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa; 
CREATE TABLE IF NOT EXISTS cities(
	state_id INT NOT NULL,
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(state_id) REFERENCES states(id)
	WHERE name = 'California';
	ORDER BY cities.id DESC
);

