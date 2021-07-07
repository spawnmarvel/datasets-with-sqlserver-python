USE TestGreenWorld;
go
CREATE SCHEMA test;
go

-- create tables
CREATE TABLE test.pump (
	p_id INT IDENTITY (1, 1) PRIMARY KEY,
	p_name VARCHAR (15) NULL,
	p_plant VARCHAR (4) NULL
);
CREATE TABLE test.criteria (
	c_id INT IDENTITY (1, 1) PRIMARY KEY,
	c_name VARCHAR (10) NOT NULL,
	c_start DATETIME NOT NULL,
	c_end DATETIME NULL,
	c_w_id INT NOT NULL,
	c_status BIT,
	FOREIGN KEY (c_w_id) REFERENCES test.pump (p_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- good, now add column p_plant
ALTER TABLE test.pump
ADD p_plant VARCHAR (4);
--good
