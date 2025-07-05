import numpy as np
import matplotlib.pyplot as plt

# Configuration
np.random.seed(42)
N = 100  # nombre de points
dt = 1.0  # intervalle de temps

# Bruit
pos_noise_std = 2.0  # écart-type du bruit sur la position
vel_noise_std = 0.5  # écart-type sur la vitesse (accélérations aléatoires)

# Initialisation
true_pos = []
true_vel = []
measured_pos = []

x, y = 0.0, 0.0
vx, vy = 1.0, 0.5

for t in range(N):
    # Accélération aléatoire
    ax = np.random.normal(0, vel_noise_std)
    ay = np.random.normal(0, vel_noise_std)

    # Mise à jour de la vitesse
    vx += ax * dt
    vy += ay * dt

    # Mise à jour de la position
    x += vx * dt
    y += vy * dt

    # Stocker la vraie position et vitesse
    true_pos.append([x, y])
    true_vel.append([vx, vy])

    # Générer la mesure bruitée
    mx = x + np.random.normal(0, pos_noise_std)
    my = y + np.random.normal(0, pos_noise_std)
    measured_pos.append([mx, my])

# Convertir en tableaux NumPy
true_pos = np.array(true_pos)
measured_pos = np.array(measured_pos)

# Affichage
plt.figure(figsize=(10, 6))
plt.plot(true_pos[:, 0], true_pos[:, 1], label='True Position', linewidth=2)
plt.scatter(measured_pos[:, 0], measured_pos[:, 1], label='Measured Position (noisy)', s=20, c='red', alpha=0.6)
plt.title('Trajectoire simulée vs observations bruitées')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.axis('equal')
plt.tight_layout()
plt.show()