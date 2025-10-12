import pandas as pd  # Importamos la librería pandas, usada para manejar y analizar datos en forma de tablas (DataFrames)
import unicodedata    # Librería estándar para manejar acentos y caracteres especiales

# Creamos datos de ejemplo con errores comunes como valores nulos, duplicados o diferencias en mayúsculas/minúsculas
data = {
    "Nombre": ["Camilo", "Sara", "Andrés", "Valentina", "camilo", None],
    "Edad": [22, 17, 25, 19, 22, 20],
    "Ciudad": ["Bogotá", "Medellín", "Cali", None, "bogota", "Cartagena"]
}

df = pd.DataFrame(data)  # Convertimos el diccionario en un DataFrame (estructura similar a una hoja de cálculo)
print("=== Datos originales ===")  # Mostramos los datos originales antes de limpiar
print(df)

# Eliminar filas con datos faltantes
df = df.dropna()  # dropna() elimina las filas que tienen valores vacíos o None

# Función para quitar tildes de texto (normalización)
def quitar_tildes(texto):
    if isinstance(texto, str):
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
        return texto
    return texto

# Eliminar duplicados (ignorando mayúsculas y tildes)
df["Nombre"] = df["Nombre"].apply(quitar_tildes).str.strip().str.capitalize()  # Limpia espacios, quita tildes y pone la primera letra en mayúscula
df["Ciudad"] = df["Ciudad"].apply(quitar_tildes).str.strip().str.capitalize()  # Hace lo mismo con las ciudades
df = df.drop_duplicates()  # Elimina registros duplicados una vez los textos están normalizados

# Filtrar mayores de edad
df = df[df["Edad"] >= 18] # Crea un nuevo DataFrame solo con las personas mayores o iguales a 18 años

# Agregar una columna de verificación
df["Puede_Participar"] = True  # Agrega una nueva columna indicando que todos pueden participar

print("\n=== Datos limpios ===")  # Mostramos el resultado final después de limpiar
print(df)

# Guardar los datos en un archivo CSV
df.to_csv("participantes_limpios.csv", index=False)  # Guarda los datos filtrados en un archivo CSV sin incluir el índice
print("\n✅ Archivo 'participantes_limpios.csv' creado correctamente.")  # Muestra mensaje de confirmación
