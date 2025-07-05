import numpy as np


class KalmanFilter:
    def __init__(self, dt, point):
        self.dt = dt
        self.E = np.matrix(
            [[point[0]], [point[1]], [point[2]], [point[3]]]
        )  # Vecteur d'état

        self.A = np.matrix(
            [
                [1, 0, self.dt, 0],  # Matrice de transition
                [0, 1, 0, self.dt],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )

        self.H = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

        self.Q = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

        self.R = np.diag(
            [4, 4, 0.25, 0.25]
        )  # R représente les incertitudes de x, y, vx, vy

        self.P = np.eye(self.A.shape[1])

    def predict(self):
        # Calcul du vecteur d'état
        self.E = np.dot(self.A, self.E)
        # Calcul de prédiction
        self.P = np.dot(np.dot(self.A, self.P), np.transpose(self.A)) + self.Q
        return self.E

    def update(self, z):
        y = z - self.H @ self.E
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)

        self.E = self.E + K @ y
        Id = np.eye(self.A.shape[0])
        self.P = (Id - K @ self.H) @ self.P
        return self.E

    def get_current_estimate(self):
        return (
            float(self.E[0, 0]),
            float(self.E[1, 0]),
            float(self.E[2, 0]),
            float(self.E[3, 0]),
        )
