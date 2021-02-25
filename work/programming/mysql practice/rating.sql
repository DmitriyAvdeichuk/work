CREATE DATABASE IF NOT EXISTS rating;
USE rating;

CREATE TABLE IF NOT EXISTS Passenger
    (passid INT PRIMARY KEY,
    passname varchar(40));
    
CREATE TABLE IF NOT EXISTS Driver
    (driverid INT PRIMARY KEY,
    drivername varchar(40));
    
CREATE TABLE IF NOT EXISTS Trip(
    id INT PRIMARY KEY,
    idPassenger INT,
    idDriver INT,
    rating INT CHECK(rating >0 and rating <6),
    cost FLOAT,
   FOREIGN KEY(idPassenger) REFERENCES Passenger(passid),
   FOREIGN KEY(idDriver) REFERENCES Driver(driverid));
   
INSERT Passenger(passid, passname)
VALUES(0, 'alex');
   
INSERT Passenger(passid, passname)
VALUES(1, 'pasha');
   
INSERT Passenger(passid, passname)
VALUES(2, 'misha');
   
INSERT Passenger(passid, passname)
VALUES(3, 'petya');
   
INSERT Passenger(passid, passname)
VALUES(4, 'antoshka');
   
INSERT Driver(driverid, drivername)
VALUES(0, 'gena');
   
INSERT Driver(driverid, drivername)
VALUES(1, 'vasya');
   
INSERT Driver(driverid, drivername)
VALUES(2, 'ara');

INSERT Driver(driverid, drivername)
VALUES(3, 'jora');

INSERT Driver(driverid, drivername)
VALUES(4, 'erjan');

INSERT Driver(driverid, drivername)
VALUES(5, 'vaga');

INSERT Driver(driverid, drivername)
VALUES(6, 'magomeg');

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(0, 0, 1, 4, 100);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(1, 0, 1, 5, 200);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(2, 0, 2, 3, 150);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(3, 1, 3, 2, 500);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(4, 4, 6, 3, 232);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(5, 3, 5, 2, 123);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(6, 2, 3, 3, 456);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(7, 4, 6, 3, 322);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(8, 3, 4, 5, 444);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(9, 2, 2, 3, 421);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(10, 0, 3, 3, 231);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(11, 0, 2, 5, 111);

INSERT trip(id, idPassenger, idDriver, rating, cost)
VALUES(12, 3, 5, 2, 5000);



SELECT DISTINCT(passname) FROM
(SELECT * FROM trip JOIN Passenger ON trip.idPassenger=Passenger.passid
JOIN Driver ON trip.idDriver = Driver.driverid ) as drivers
WHERE drivername = 'ara';


SELECT DISTINCT(driver.drivername) FROM
(SELECT * FROM trip JOIN Passenger ON trip.idPassenger=Passenger.passid
JOIN Driver ON trip.idDriver = Driver.driverid ) as ewq
WHERE drivername NOT IN (SELECT drivername FROM trip
JOIN Driver ON trip.idDriver = Driver.driverid
WHERE RATING <=2);


SELECT passname, COUNT(*) AS tripcount FROM (SELECT * FROM trip JOIN Passenger ON trip.idPassenger=Passenger.passid
JOIN Driver ON trip.idDriver = Driver.driverid ) AS drivers
GROUP BY passname;


SELECT passname, COUNT(*) AS tripcount FROM (SELECT * FROM trip JOIN Passenger ON trip.idPassenger=Passenger.passid
JOIN Driver ON trip.idDriver = Driver.driverid ) AS drivers
GROUP BY passname
ORDER BY tripcount DESC
LIMIT 1;

