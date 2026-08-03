import pandas as pd
from geopy.distance import geodesic

locations = pd.read_csv("../data/hyderabad_locations.csv")

start = "Hitech City"
end = "Gachibowli"

start_row = locations[locations["location_name"] == start].iloc[0]
end_row = locations[locations["location_name"] == end].iloc[0]

coord_1 = (start_row["latitude"], start_row["longitude"])
coord_2 = (end_row["latitude"], end_row["longitude"])

distance = geodesic(coord_1, coord_2).kilometers

print(f"Distance: {distance:.2f} km")