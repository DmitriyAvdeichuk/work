use rating;

SELECT passname, COUNT(*) AS tripcount FROM (SELECT * FROM trip JOIN Passenger ON trip.idPassenger=Passenger.passid
JOIN Driver ON trip.idDriver = Driver.driverid ) AS drivers
GROUP BY passname
ORDER BY tripcount DESC
LIMIT 1;
