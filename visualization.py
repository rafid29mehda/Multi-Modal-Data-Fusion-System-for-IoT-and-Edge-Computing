import matplotlib.pyplot as plt
import pandas as pd

# Load the sensor data
sensor_df = pd.read_csv('sensor_data.csv')

# Plot the fused temperature and GPS data
plt.figure(figsize=(10, 6))

# Plot temperature over time
plt.subplot(2, 1, 1)
plt.plot(sensor_df['timestamp'], sensor_df['temperature'], label="Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature over Time")

# Plot GPS data over time (latitude)
plt.subplot(2, 1, 2)
plt.plot(sensor_df['timestamp'], sensor_df['latitude'], label="Latitude", color='red')
plt.xlabel("Time")
plt.ylabel("Latitude")
plt.title("GPS Latitude over Time")

plt.tight_layout()
plt.show()
