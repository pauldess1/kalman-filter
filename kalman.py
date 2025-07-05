import numpy as np

class KalmanFilter():
    def __init__(self, dt, point):
        self.dt = dt
        self.E = np.matrix([[point[0], point[1], 0, 0]]) # Vecteur d'état

        self.A = np.matrix([[1, 0, self.dt, 0],  # Matrice de transition
                           [0, 1, 0, self.dt],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        
        self.H = np.matrix([[1, 0, 0, 0],    # Matrice d'observation (on observe que x et y)
                           [0, 1, 0, 0]])
        
        self.Q = np.matrix([[1, 0, 0, 0],
                           [0, 1, 0, 0],
                           [0, 0, 1, 0],
                           [0, 0, 0, 1]])
        
        self.R = np.matrix([[1, 0],
                           [0, 1]])
        
        self.P = np.eye(self.A.shape[1])
    
    def predict(self):
        # Calcul du vecteur d'état
        self.E = np.dot(self.A, self.E)
        # Calcul de prédiction
        self.P = np.dot(np.dot(self.A, self.P), np.transpose(self.A)) + self.Q
        return self.E