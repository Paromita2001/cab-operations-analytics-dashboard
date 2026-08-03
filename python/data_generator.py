import pandas as pd
import random
from faker import Faker
from geopy.distance import geodesic

fake = Faker("en_IN")

# Load locations
locations_df = pd.read_csv("../data/hyderabad_locations.csv")

cab_types = ["Mini", "Sedan", "SUV", "Auto", "Bike"]

payment_methods = [
    "UPI",
    "Cash",
    "Credit Card",
    "Debit Card",
    "Wallet"
]

weather_conditions = [
    "Sunny",
    "Cloudy",
    "Rainy"
]

base_rates = {
    "Mini": 12,
    "Sedan": 16,
    "SUV": 20,
    "Auto": 10,
    "Bike": 8
}

fuel_rates = {
    "Mini": 4,
    "Sedan": 5,
    "SUV": 7,
    "Auto": 3,
    "Bike": 2
}

data = []

for trip_id in range(1, 25001):

    pickup_row = locations_df.sample(1).iloc[0]
    drop_row = locations_df.sample(1).iloc[0]

    while pickup_row["location_name"] == drop_row["location_name"]:
        drop_row = locations_df.sample(1).iloc[0]

    pickup = pickup_row["location_name"]
    drop = drop_row["location_name"]

    distance = round(
        geodesic(
            (pickup_row["latitude"], pickup_row["longitude"]),
            (drop_row["latitude"], drop_row["longitude"])
        ).km,
        2
    )

    trip_hour = random.randint(0, 23)

    trip_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    trip_date = pd.to_datetime(trip_date).strftime("%Y-%m-%d")

    trip_day = pd.to_datetime(trip_date).strftime("%A")

    is_weekend = 1 if trip_day in [
        "Saturday",
        "Sunday"
    ] else 0

    weather = random.choice(weather_conditions)

    cab_type = random.choice(cab_types)

    travel_time = max(1, int(distance / 25 * 60))

    surge_multiplier = 1.0

    if 8 <= trip_hour <= 10 or 18 <= trip_hour <= 21:
        surge_multiplier += 0.5

    if weather == "Rainy":
        surge_multiplier += 0.2

    fare = round(
        distance * base_rates[cab_type] * surge_multiplier,
        2
    )

    fuel_cost = round(
        distance * fuel_rates[cab_type],
        2
    )

    profit = round(
        fare - fuel_cost,
        2
    )

    data.append({

        "trip_id": trip_id,
        "trip_date": trip_date,
        "trip_day": trip_day,
        "is_weekend": is_weekend,
        "trip_hour": trip_hour,
        "weather": weather,
        "pickup_city": "Hyderabad",
        "pickup_location": pickup,
        "drop_location": drop,
        "cab_type": cab_type,
        "distance_km": distance,
        "travel_time_min": travel_time,
        "fare": fare,
        "fuel_cost": fuel_cost,
        "profit": profit,
        "payment_method": random.choice(payment_methods),
        "driver_id": random.randint(1000, 1500),
        "driver_rating": round(random.uniform(3.5, 5.0), 1),
        "customer_rating": round(random.uniform(3.0, 5.0), 1),
        "surge_multiplier": surge_multiplier

    })

df = pd.DataFrame(data)

df.to_csv("../data/trips.csv", index=False)

print("✅ trips.csv generated successfully!")