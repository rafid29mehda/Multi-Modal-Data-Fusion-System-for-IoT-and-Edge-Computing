import random
import time
import pandas as pd

# Function to simulate temperature sensor data
def generate_temperature_data():
    temperature = random.uniform(15.0, 30.0)  # Simulate temperature between 15 to 30°C
    return temperature

# Function to simulate GPS coordinates
def generate_gps_data():
    latitude = random.uniform(-90, 90)  # Latitude range
    longitude = random.uniform(-180, 180)  # Longitude range
    return latitude, longitude

# Create an empty list to store data
sensor_data = []

# Collect data for 100 samples
for i in range(100):
    temp_data = generate_temperature_data()
    gps_data = generate_gps_data()
    timestamp = time.time()
    sensor_data.append({"timestamp": timestamp, "temperature": temp_data, "latitude": gps_data[0], "longitude": gps_data[1]})
    time.sleep(0.1)  # Simulate time delay between sensor readings

# Convert the list to a pandas dataframe for easy visualization
sensor_df = pd.DataFrame(sensor_data)

# Show the first 5 rows
sensor_df.head()

# Save the simulated data to a CSV file (optional)
sensor_df.to_csv('sensor_data.csv', index=False)
