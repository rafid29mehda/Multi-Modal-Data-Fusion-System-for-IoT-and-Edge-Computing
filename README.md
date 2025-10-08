# Multi-Modal Data Fusion System for IoT and Edge Computing

This project simulates an IoT-based system that collects data from various sensors (temperature and GPS), processes it at the edge using machine learning techniques, and visualizes the data using real-time analytics. The system also demonstrates sensor data fusion and communication protocols for smart systems and edge AI applications.

## Key Features

* **Sensor Integration**: Simulates data from temperature and GPS sensors.
* **Edge Processing**: Uses TensorFlow to process data at the edge (simulated using Google Colab).
* **Communication Layer**: Emulates a basic socket server to demonstrate communication between devices.
* **Analytics and Fusion**: Implements a Kalman filter for sensor fusion and processes the data.
* **Visualization**: Uses `matplotlib` to visualize the temperature and GPS data.
* **Machine Learning**: A simple neural network model is trained on the sensor data for binary classification.

## Technologies Used

* **Python**: Primary language for the project.
* **TensorFlow**: For edge processing and machine learning.
* **NumPy**: For numerical operations.
* **pandas**: For handling sensor data in DataFrame format.
* **Matplotlib**: For visualizing the data.
* **Socket Programming**: For communication between the edge device and server.
* **Kalman Filter**: For sensor data fusion.

## Project Structure

* `sensor_data_simulation.py`: Simulates data from IoT sensors (temperature and GPS).
* `edge_processing.py`: Contains the neural network model using TensorFlow.
* `communication_layer.py`: Implements a basic socket server for communication.
* `kalman_filter.py`: Implements Kalman filtering for sensor data fusion.
* `visualization.py`: Visualizes the fused data using `matplotlib`.

## Setup and Installation

To run this project, follow these steps:

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/multi-modal-data-fusion.git
cd multi-modal-data-fusion
```

### Step 2: Install Dependencies

Create a virtual environment (optional but recommended) and install the required packages:

```bash
pip install -r requirements.txt
```

### Step 3: Run the Project

1. **Sensor Data Simulation**: Run the script to simulate IoT sensor data.

   ```bash
   python sensor_data_simulation.py
   ```

2. **Edge Processing**: Train the neural network on the simulated sensor data.

   ```bash
   python edge_processing.py
   ```

3. **Communication Layer**: Start the socket server (run in a separate terminal).

   ```bash
   python communication_layer.py
   ```

4. **Kalman Filter**: Test the sensor fusion using the Kalman filter.

   ```bash
   python kalman_filter.py
   ```

5. **Visualization**: Plot the temperature and GPS data.

   ```bash
   python visualization.py
   ```

### Step 4: View Results

After running the scripts, you will see:

* A plot of **Temperature** and **GPS Latitude** over time.
* The **updated state estimate** after applying the Kalman filter to the sensor data.
* A message from the server acknowledging data communication.

