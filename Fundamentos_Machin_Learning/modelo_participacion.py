import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# 1️ Cargar los datos limpios
df = pd.read_csv("participantes_limpios.csv")

# 2️ Crear una columna objetivo (1 = puede participar, 0 = no)
df["puede_participar"] = df["Edad"].apply(lambda x: 1 if x >= 18 else 0)

# 3️ Seleccionar las columnas para entrenar el modelo
X = df[["Edad"]]       # Características
y = df["puede_participar"]  # Objetivo

# 4️ Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 5️ Crear el modelo
modelo = DecisionTreeClassifier()

# 6️ Entrenar el modelo
modelo.fit(X_train, y_train)

# 7️ Hacer predicciones
predicciones = modelo.predict(X_test)

# 8️ Evaluar el modelo
precision = accuracy_score(y_test, predicciones)
print(f"Precisión del modelo: {precision:.2f}")

print("\nMatriz de confusión:")
print(confusion_matrix(y_test, predicciones))

# 9️ Probar el modelo con nuevos datos
nueva_edad = int(input("\nIngrese una edad para predecir: "))
resultado = modelo.predict([[nueva_edad]])

if resultado[0] == 1:
    print(" Puede participar en SENASOFT")
else:
    print(" No puede participar en SENASOFT")
