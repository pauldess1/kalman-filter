from generate_data import generate_trajectory
from kalman import KalmanFilter
from plot_utils import plot_with_plotly
import numpy as np

true, measured = generate_trajectory()
dt = 1.0

# Initialisation du filtre avec le premier vecteur complet (x, y, vx, vy)
kf = KalmanFilter(dt, measured[0])
predicted_pos = []

for z in measured:
    # Création du vecteur mesure 4x1 : position + vitesse
    z_meas = np.matrix([[z[0]], [z[1]], [z[2]], [z[3]]])
    kf.predict()
    kf.update(z_meas)
    predicted_pos.append(kf.get_current_estimate())

predicted_pos = np.array(predicted_pos)
plot_with_plotly(true, measured, predicted_pos)
