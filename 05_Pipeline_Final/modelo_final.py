import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 1. Cargar el Dataset
df = pd.read_csv("titanic.csv")

# 2. Seleccionar características y target
# Usaremos las 3 columnas numéricas que ya limpiamos
X = df[['Age', 'Fare']]
y = df['Survived']

# Rellenar nulos en Y para simplificar (aunque no es la mejor práctica, lo hacemos por consistencia del ejemplo)
y = y.fillna(0) # Reemplazamos nulos en Survived con 0 (No Sobrevivió)

# 3. División de Datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# 4. CREAR EL PIPELINE (La tubería de trabajo)
# Encadenamos los pasos en orden: Imputar -> Escalar -> Modelar
modelo_pasos = [
    ('imputer', SimpleImputer(strategy='mean')), # 1. Rellenar nulos
    ('scaler', StandardScaler()),                 # 2. Estandarizar
    ('knn', KNeighborsClassifier(n_neighbors=5))  # 3. El clasificador (k=5)
]

# Definir el Pipeline
pipeline = Pipeline(modelo_pasos)

# 5. Entrenar el Pipeline (El .fit() hace los 3 pasos automáticamente en X_train)
pipeline.fit(X_train, y_train)

# 6. Evaluar con Validación Cruzada (La evaluación más robusta)
# cv=10 para una evaluación muy fuerte
cv_scores = cross_val_score(pipeline, X, y, cv=10, scoring='accuracy')

print("--- Resultado Final del Modelo (Listo para Competencia) ---")
print(f"Accuracy de cada Fold (10 pruebas): {cv_scores}")
print(f"Accuracy PROMEDIO y ROBUSTO: {np.mean(cv_scores):.4f}")