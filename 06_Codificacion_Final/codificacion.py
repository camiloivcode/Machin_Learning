import pandas as pd
from sklearn.impute import SimpleImputer 

# Cargar el Dataset
url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
df = pd.read_csv(url)

# 1. Identificar columnas categóricas a codificar
columnas_categoricas = ['Sex', 'Embarked']

# 2. Imputación de nulos en 'Embarked' (Usamos la moda - el valor más frecuente)
# Esto es necesario antes de la codificación.
imputer_moda = SimpleImputer(strategy='most_frequent')

# Ajusta el imputer y transforma la columna 'Embarked'
df['Embarked'] = imputer_moda.fit_transform(df[['Embarked']])


# 3. Aplicar One-Hot Encoding
# drop_first=True elimina una columna para evitar la multicolinealidad.
df_codificado = pd.get_dummies(df, columns=columnas_categoricas, drop_first=True) 

# 4. Mostrar los resultados
print("--- Columnas DESPUÉS de la Codificación ---")
print(df_codificado.head())
print("\nColumnas Creadas para 'Sex' y 'Embarked':")
print([col for col in df_codificado.columns if 'Sex_' in col or 'Embarked_' in col])