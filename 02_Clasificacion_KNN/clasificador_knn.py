# Importamos las librerías
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# 1. Cargar el dataset (¡fácil con sklearn!)
iris = load_iris()
X, y = iris.data, iris.target

# 2. Dividir los datos en entrenamiento y prueba
# El 30% lo reservamos para probar qué tan bien le va al modelo
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Crear el modelo de Clasificación (Usaremos 3 vecinos)
# El parámetro 'n_neighbors=3' es nuestro 'k'
knn = KNeighborsClassifier(n_neighbors=3)

# 4. Entrenar el modelo
knn.fit(X_train, y_train)

# 5. Hacer predicciones en los datos de prueba
y_pred = knn.predict(X_test)

# 6. Evaluar el modelo (¿Qué porcentaje de aciertos tuvo?)
precision = accuracy_score(y_test, y_pred)

print(f"El modelo KNN tuvo una precisión (Accuracy) de: {precision:.2f}") 
# Si el resultado es 1.00, ¡el modelo clasificó el 100% de las flores correctamente!