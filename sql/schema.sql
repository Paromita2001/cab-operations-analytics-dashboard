CREATE TABLE trips (

    trip_id INT PRIMARY KEY,

    trip_date DATE,

    trip_day VARCHAR(20),

    is_weekend BOOLEAN,

    trip_hour INT,

    weather VARCHAR(20),

    pickup_city VARCHAR(50),

    pickup_location VARCHAR(100),

    drop_location VARCHAR(100),

    cab_type VARCHAR(20),

    distance_km FLOAT,

    travel_time_min INT,

    fare FLOAT,

    payment_method VARCHAR(30),

    driver_id INT,

    driver_rating FLOAT,

    customer_rating FLOAT,

    surge_multiplier FLOAT,

    fuel_cost FLOAT,

    profit FLOAT

);