from generate_data import generate_trajectory
from kalman import KalmanFilter

true_pos, measured_pos = generate_trajectory()
# print(true_pos, measured_pos)

kalman_filter = KalmanFilter()
