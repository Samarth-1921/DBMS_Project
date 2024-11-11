CREATE DATABASE IF NOT EXISTS CollegesDB;
USE CollegesDB;

CREATE TABLE Colleges (
    college_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    established_year INT,
    contact_email VARCHAR(255),
    contact_phone VARCHAR(20),
    website VARCHAR(255)
);
INSERT INTO Colleges (name, location, established_year, contact_email, contact_phone, website)
VALUES 
('Example Engineering College', 'City A, State B', 2005, 'contact@examplecollege.com', '1234567890', 'http://www.examplecollege.com'),
('Tech Institute', 'City C, State D', 2010, 'info@techinstitute.com', '0987654321', 'http://www.techinstitute.com'),
('Private Engineering School', 'City E, State F', 1998, 'admissions@pes.com', '1122334455', 'http://www.pes.com');

SELECT * FROM Colleges
INTO OUTFILE 'explore.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';
