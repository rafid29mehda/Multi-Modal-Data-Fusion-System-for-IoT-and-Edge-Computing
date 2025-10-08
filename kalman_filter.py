import numpy as np

# Kalman Filter implementation for temperature and GPS fusion
def kalman_filter(z, x_prev, P_prev):
    F = np.array([[1, 0], [0, 1]])  # State transition matrix (simplified)
    H = np.array([[1, 0], [0, 1]])  # Measurement matrix (simplified)
    R = np.array([[0.1, 0], [0, 0.1]])  # Measurement noise covariance (simplified)
    Q = np.array([[0.1, 0], [0, 0.1]])  # Process noise covariance (simplified)

    # Prediction
    x_pred = np.dot(F, x_prev)
    P_pred = np.dot(F, np.dot(P_prev, F.T)) + Q

    # Update
    y = z - np.dot(H, x_pred)  # Innovation
    S = np.dot(H, np.dot(P_pred, H.T)) + R  # Innovation covariance
    K = np.dot(P_pred, np.dot(H.T, np.linalg.inv(S)))  # Kalman gain

    x_new = x_pred + np.dot(K, y)
    P_new = P_pred - np.dot(K, np.dot(H, P_pred))

    return x_new, P_new

# Test Kalman Filter with simulated data
z = np.array([30.5, 40.7])  # Simulated temperature and GPS data
x_prev = np.array([30, 40])  # Initial state estimate
P_prev = np.array([[1, 0], [0, 1]])  # Initial covariance

x_new, P_new = kalman_filter(z, x_prev, P_prev)
print("Updated state estimate:", x_new)
