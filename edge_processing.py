import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

# Load the simulated sensor data (you can replace this with actual file reading)
sensor_df = pd.read_csv('sensor_data.csv')

# Ensure sensor_features and sensor_labels are NumPy arrays
sensor_features = np.array(sensor_df[['temperature', 'latitude']])  # Input features
sensor_labels = np.array([random.randint(0, 1) for _ in range(len(sensor_features))])  # Random labels for classification

# Check the types of the arrays
print(type(sensor_features))  # Should be <class 'numpy.ndarray'>
print(type(sensor_labels))  # Should be <class 'numpy.ndarray'>

# Create a simple neural network model
model = tf.keras.Sequential([
    layers.Input(shape=(2,)),  # Specify the input shape (2 features)
    layers.Dense(32, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(sensor_features, sensor_labels, epochs=3)

# Save the trained model (optional)
model.save('sensor_model.h5')
