-- Total trips
SELECT COUNT(*) AS total_trips FROM trips;

-- Total revenue
SELECT SUM(fare) AS total_revenue FROM trips;

-- Total profit
SELECT SUM(profit) AS total_profit FROM trips;

-- Revenue by cab type
SELECT cab_type, SUM(fare) AS revenue
FROM trips
GROUP BY cab_type;

-- Peak-hour demand
SELECT trip_hour, COUNT(*) AS trips
FROM trips
GROUP BY trip_hour;

-- Revenue by weather
SELECT weather, SUM(fare) AS revenue
FROM trips
GROUP BY weather;