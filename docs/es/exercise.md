# Ejercicio: análisis y predicción de ventas minoristas

## Contexto

En el sector minorista, la inteligencia artificial puede ayudar a optimizar las
operaciones comerciales y a tomar decisiones informadas. En esta práctica se
utilizará un conjunto de datos ficticio con ventas de varias tiendas minoristas
en distintas ciudades y años.

El objetivo es analizar los datos, preprocesarlos, calcular métricas relevantes,
visualizar los resultados y construir un modelo que estime las ventas.

## Objetivos

### Manipulación de datos con Pandas

- Importar y explorar el conjunto de datos.
- Limpiar los datos y manejar valores faltantes.
- Agrupar los datos y calcular métricas estadísticas.
- Crear un gráfico de barras con las ventas totales por ciudad y año.

### Uso de NumPy

- Normalizar las ventas para su análisis posterior.

### Predicción con Scikit-learn

- Dividir los datos en conjuntos de entrenamiento y prueba.
- Entrenar un modelo de regresión lineal para predecir ventas.
- Evaluar el modelo con métricas adecuadas, como el error cuadrático medio.

## Instrucciones

### 1. Preparar el entorno

Importa las bibliotecas necesarias:

- NumPy
- Pandas
- Matplotlib
- Scikit-learn

### 2. Crear el DataFrame

Crea el DataFrame directamente a partir de los datos proporcionados. Cada
diccionario representa una fila:

```python
import pandas as pd

records = [
    {"Ciudad": "Madrid", "Año": 2021, "Mes": "Enero", "Ventas": 1500},
    {"Ciudad": "Barcelona", "Año": 2021, "Mes": "Enero", "Ventas": 2000},
    {"Ciudad": "Valencia", "Año": 2021, "Mes": "Enero", "Ventas": 1800},
    {"Ciudad": "Madrid", "Año": 2021, "Mes": "Febrero", "Ventas": 1700},
    {"Ciudad": "Barcelona", "Año": 2021, "Mes": "Febrero", "Ventas": 2100},
    {"Ciudad": "Valencia", "Año": 2021, "Mes": "Febrero", "Ventas": 1900},
    {"Ciudad": "Madrid", "Año": 2022, "Mes": "Enero", "Ventas": 1600},
    {"Ciudad": "Barcelona", "Año": 2022, "Mes": "Enero", "Ventas": 2200},
    {"Ciudad": "Valencia", "Año": 2022, "Mes": "Enero", "Ventas": 2000},
    {"Ciudad": "Madrid", "Año": 2022, "Mes": "Febrero", "Ventas": 1800},
    {"Ciudad": "Barcelona", "Año": 2022, "Mes": "Febrero", "Ventas": 2300},
    {"Ciudad": "Valencia", "Año": 2022, "Mes": "Febrero", "Ventas": 2100},
]

dataframe = pd.DataFrame(records)
```

`Año` y `Ventas` serán numéricos; `Ciudad` y `Mes` serán texto. Convierte
`Mes` a una representación numérica o categórica cuando prepares las variables
del modelo.

### 3. Explorar y limpiar los datos

- Inspecciona el DataFrame y comprueba si hay valores faltantes.
- Calcula estadísticas descriptivas de las ventas, como la media y la mediana.

### 4. Agrupar y visualizar los datos

- Agrupa las ventas por ciudad y año para calcular los totales anuales.
- Representa los datos agregados en un gráfico de barras.
- Añade al gráfico un título y etiquetas adecuados.
- Muestra las ventas totales por ciudad y año.

### 5. Preprocesar los datos con NumPy

Normaliza al rango `[0, 1]` las ventas totales calculadas en el paso anterior.

### 6. Crear y evaluar un modelo predictivo

- Transforma la variable `Mes` en valores numéricos.
- Utiliza `Año` y `Mes` como variables predictoras de las ventas.
- Crea un modelo de regresión lineal con Scikit-learn.
- Divide los datos en un conjunto de entrenamiento (80 %) y uno de prueba (20 %).
- Evalúa el modelo con métricas como el error cuadrático medio (MSE).

### 7. Presentar conclusiones

- Interpreta los resultados del análisis y del modelo predictivo.
- Explica cómo podrían ayudar estos resultados a un gerente de tienda a tomar
  decisiones.
