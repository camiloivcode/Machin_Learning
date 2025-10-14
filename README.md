# 🤖 Ruta de Aprendizaje: Machine Learning para SENA Soft IA

## 🌟 Descripción General

Este repositorio documenta mi progreso y desarrollo de habilidades en **Machine Learning (ML)**. El contenido está enfocado en dominar el **flujo de trabajo completo** de ML, desde la limpieza de datos hasta la evaluación robusta de modelos, como preparación para la competencia **SENA Soft IA 2024**.

El aprendizaje se centra en la aplicación práctica de algoritmos esenciales de clasificación y regresión, y en técnicas cruciales como el **Pipeline** y la **Validación Cruzada**.

---

## 🗺️ Estructura del Proyecto y Conceptos Aprendidos

El repositorio está organizado en módulos secuenciales que siguen el flujo de un proyecto de ML real.

| Carpeta | Tópico Principal | Habilidades y Algoritmos Desarrollados | Dataset de Ejemplo |
| :--- | :--- | :--- | :--- |
| `01_Regresion_Lineal_Simple` | **Fundamentos de Regresión** | Entendimiento de $X$ (Features) y $Y$ (Target), Modelo de Regresión Lineal. | Horas de Estudio vs. Nota |
| `02_Clasificacion_KNN` | **Fundamentos de Clasificación** | Algoritmo **k-Nearest Neighbors (KNN)**, Métrica de `accuracy_score`. | Iris |
| `03_Validacion_Cruzada` | **Evaluación Robusta** | Prevención de **Overfitting**, Uso de **Validación Cruzada** (`cross_val_score`), Interpretación de Desviación Estándar. | Iris |
| `04_Preprocesamiento_Escalado` | **Preprocesamiento ETL** | **Imputación** de valores nulos, **Estandarización** (`StandardScaler`) para algoritmos basados en distancia. | Titanic |
| `05_Pipeline_Final` | **Modelo de Competencia** | Creación de un **Pipeline** para encadenar (`Imputer` $\rightarrow$ `Scaler` $\rightarrow$ `KNN`), Evaluación final con 10-Fold CV. | Titanic |

---

## 🛠️ Stack Tecnológico

* **Lenguaje de Programación:** Python
* **Librerías Clave:**
    * **`pandas` y `numpy`**: Manipulación y manejo eficiente de datos.
    * **`scikit-learn (sklearn)`**: Implementación de algoritmos, preprocesamiento (`SimpleImputer`, `StandardScaler`), y creación de flujos de trabajo (`Pipeline`).

---

## 🎯 Objetivo para SENA Soft IA

El objetivo es aplicar la metodología del **Pipeline** y la **Validación Cruzada** en el dataset de la competencia para garantizar que el modelo sea:

1.  **Justo:** Aplicando preprocesamiento (`StandardScaler`).
2.  **Robusto:** Evaluado con `cross_val_score`.
3.  **Eficiente:** Usando el flujo encadenado de un `Pipeline`.