# Importamos las librerías necesarias
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

# 1. Cargar el dataset (usamos el mismo de Iris, pero AHORA NO HACEMOS train_test_split)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Crear el modelo de Clasificación (KNN con 3 vecinos)
knn = KNeighborsClassifier(n_neighbors=3)

# 3. Aplicar Cross-Validation (Validación Cruzada)
# cv=5 significa que dividiremos el dataset en 5 partes (folds)
# scoring='accuracy' indica que queremos medir la precisión
scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')

# 4. Imprimir los resultados
print(f"Resultados de Accuracy por cada Fold (5 Folds): {scores}")
print(f"Accuracy PROMEDIO (Evaluación más robusta): {np.mean(scores):.4f}")
print(f"Desviación Estándar (Qué tan variables son los resultados): {np.std(scores):.4f}")