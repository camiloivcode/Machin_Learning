import pandas as pd  # Importamos la librería pandas para manejar datos en forma de tablas

# Creamos un DataFrame con datos de ejemplo
data = {
    "Nombre": ["Camilo", "Sara", "Andrés", "Valentina"],
    "Edad": [22, 17, 25, 19],
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Bogotá"]
}

df = pd.DataFrame(data)  # Convertimos el diccionario en un DataFrame (tabla de pandas)

# print(df)  # (opcional) muestra toda la tabla completa

# Filtrar datos (igual que hicimos con listas)
mayores = df[df["Edad"] >= 18]  # Crea un nuevo DataFrame solo con las personas mayores de edad
print(f"Las personas mayores de edad son:\n{mayores}")  # Muestra en pantalla los mayores de edad

# Guardar los datos en un archivo CSV
mayores.to_csv("participantes_validos.csv", index=False)  # Guarda los datos filtrados en un archivo CSV
print("Archivo guardado como participantes_validos.csv ✅")  # Mensaje de confirmación

# Leer nuevamente el archivo CSV guardado
df = pd.read_csv("participantes_validos.csv")  # Carga el archivo CSV en un nuevo DataFrame
print(df.head())  # Muestra las primeras 5 filas del archivo para verificar que se guardó bien
