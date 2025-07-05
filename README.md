# Projet Filtre de Kalman (Kalman Filter)

Ce projet a pour objectif de comprendre et d’implémenter un filtre de Kalman simple appliqué à une trajectoire 2D avec position et vitesse.

## Description

Le filtre de Kalman est un algorithme récursif utilisé pour estimer l’état d’un système dynamique à partir de mesures bruitées. Ici, nous modélisons un objet en mouvement dans un plan (x, y) avec une vitesse (vx, vy).

Le projet comprend :  
- La génération d’une trajectoire simulée avec bruit sur les positions et les vitesses mesurées.  
- Une classe `KalmanFilter` implémentant la prédiction et la mise à jour de l’état.  
- Un script principal qui applique le filtre aux mesures simulées.  
- Une visualisation interactive avec Plotly affichant les trajectoires vraie, mesurée, et estimée.

## Utilisation

1. Générer une trajectoire simulée avec bruit.  
2. Initialiser le filtre de Kalman avec un état initial basé sur les premières mesures.  
3. Parcourir les mesures pour effectuer les étapes de prédiction et mise à jour du filtre.  
4. Visualiser les trajectoires à l’aide de Plotly.

## TODO

- [ ] Tracer l’évolution des valeurs internes du filtre de Kalman (matrice de covariance `P`, gain de Kalman `K`, erreur d’estimation) au cours du temps.  
- [ ] Tester différentes configurations des matrices de bruit `Q` et `R` pour étudier leur effet sur la précision et la réactivité du filtre.  
- [ ] Étendre le modèle à des cas plus complexes (intégration d’une accélération, mesures partielles, filtre de Kalman étendu pour systèmes non linéaires).

## Technologies utilisées

- Python 3  
- NumPy pour les calculs matriciels  
- Plotly pour la visualisation interactive  
