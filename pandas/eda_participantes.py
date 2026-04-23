import pandas as pd
import matplotlib.pyplot as plt

# 1️ Cargar los datos limpios
df = pd.read_csv("participantes_limpios.csv")

print("=== Vista general del dataset ===")
print(df.head())

# 2️ Información general del DataFrame
print("\n=== Información del dataset ===")
print(df.info())

# 3️ Estadísticas descriptivas
print("\n=== Estadísticas ===")
print(df.describe())

# Histograma de edades
plt.hist(df["Edad"], bins=5)
plt.title("Distribución de edades de participantes")
plt.xlabel("Edad")
plt.ylabel("Cantidad de personas")
plt.show()

# 4️ Conteo de participantes por ciudad
conteo_ciudades = df["Ciudad"].value_counts()
print("\n=== Participantes por ciudad ===")
print(conteo_ciudades)

conteo_ciudades.plot(kind="bar", color="skyblue")
plt.title("Cantidad de participantes por ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Cantidad")
plt.show()

print("\n=== Correlaciones numéricas ===")
print(df.corr(numeric_only=True))

