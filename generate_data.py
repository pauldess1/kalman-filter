import numpy as np


def generate_trajectory():
    # Configuration
    np.random.seed(42)
    N = 100  # nombre de points
    dt = 1.0  # intervalle de temps

    # Bruit
    pos_noise_std = 2.0  # bruit sur la position mesurée
    vel_noise_std = 0.5  # bruit sur l'accélération vraie
    vel_meas_noise_std = 0.8  # bruit sur la mesure de vitesse

    # Initialisation
    true_pos = []
    true_vel = []
    measured_pos = []
    measured_vel = []

    x, y = 0.0, 0.0
    vx, vy = 1.0, 0.5

    for _ in range(N):
        # Accélération aléatoire (modèle de mouvement)
        ax = np.random.normal(0, vel_noise_std)
        ay = np.random.normal(0, vel_noise_std)

        # Mise à jour de la vitesse
        vx += ax * dt
        vy += ay * dt

        # Mise à jour de la position
        x += vx * dt
        y += vy * dt

        # Stockage des valeurs vraies
        true_pos.append([x, y])
        true_vel.append([vx, vy])

        # Génération des mesures bruitées
        mx = x + np.random.normal(0, pos_noise_std)
        my = y + np.random.normal(0, pos_noise_std)
        measured_pos.append([mx, my])

        mvx = vx + np.random.normal(0, vel_meas_noise_std)
        mvy = vy + np.random.normal(0, vel_meas_noise_std)
        measured_vel.append([mvx, mvy])

    # Conversion en tableaux NumPy
    true_pos = np.array(true_pos)
    true_vel = np.array(true_vel)
    measured_pos = np.array(measured_pos)
    measured_vel = np.array(measured_vel)

    true = np.concatenate((true_pos, true_vel), axis=1)
    measured = np.concatenate((measured_pos, measured_vel), axis=1)

    return true, measured
