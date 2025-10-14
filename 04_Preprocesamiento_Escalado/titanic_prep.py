import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer # Para manejar nulos

# Cargar el Dataset (Puedes descargarlo de Kaggle o usar este enlace directo)
df = pd.read_csv("titanic.csv")

# 1. Seleccionar solo las características numéricas relevantes y el Target
# Edad (Age) y Tarifa (Fare) tienen diferentes escalas. Sobrevivió (Survived) es el target.
df = df[['Age', 'Fare', 'Survived']].copy()

# 2. Manejo de Valores Nulos (Imputación)
# Reemplazar los valores faltantes (NaN) en Age y Fare con la media de la columna
imputer = SimpleImputer(strategy='mean')
df[['Age', 'Fare']] = imputer.fit_transform(df[['Age', 'Fare']])

# 3. Separar X (features) y Y (target)
X = df[['Age', 'Fare']]
y = df['Survived']

# 4. Aplicar Estandarización a X
# El StandardScaler se ajusta (fit) a los datos de entrenamiento para obtener mu y sigma,
# y luego se usa para transformar los datos de entrenamiento y prueba.
scaler = StandardScaler()

# Transformar los datos
X_scaled = scaler.fit_transform(X)
X_scaled_df = pd.DataFrame(X_scaled, columns=['Age_Scaled', 'Fare_Scaled'])


# 5. Imprimir los resultados (Opcional, pero útil para verificar)
print("--- Primeras 5 filas ANTES de escalar (rangos diferentes) ---")
print(X.head())
print("\n--- Primeras 5 filas DESPUÉS de escalar (media ≈ 0, desv. est. ≈ 1) ---")
print(X_scaled_df.head())