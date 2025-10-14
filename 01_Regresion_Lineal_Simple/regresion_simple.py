# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 1. Creamos datos simples (Relación: a mayor estudio, mayor nota)
horas_estudio = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1) # X (Característica)
nota_examen = np.array([2, 3, 4, 4, 5, 6, 7, 8, 9, 10])               # Y (Target/Objetivo)

# 2. Creamos el modelo de Regresión Lineal
modelo = LinearRegression()

# 3. Entrenamos el modelo (Le decimos al modelo que aprenda la relación)
modelo.fit(horas_estudio, nota_examen)

# 4. Hacemos una predicción
# Preguntamos: ¿Qué nota obtendría alguien que estudia 5.5 horas?
prediccion_5_5_horas = modelo.predict([[5.5]]) 

# 5. Imprimimos el resultado (opcional)
print(f"Predicción para 5.5 horas de estudio: {prediccion_5_5_horas[0]:.2f}")

# 6. (Opcional) Graficamos la línea que el modelo "aprendió"
plt.scatter(horas_estudio, nota_examen, color='blue', label='Datos Reales')
plt.plot(horas_estudio, modelo.predict(horas_estudio), color='red', label='Línea de Regresión')
plt.title('Regresión Lineal Simple')
plt.xlabel('Horas de Estudio')
plt.ylabel('Nota del Examen')
plt.legend()
plt.show()