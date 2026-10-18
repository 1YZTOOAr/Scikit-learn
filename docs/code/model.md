# `model.py`: entrenar y evaluar la regresión

Código fuente: [`src/retail_sales/model.py`](../../src/retail_sales/model.py).

## Propósito y alcance

`SalesPredictor` divide los registros mensuales en entrenamiento y prueba, ajusta una regresión lineal y calcula el error sobre los registros reservados. Por decisión del ejercicio, usa únicamente `Año` y `Mes` como predictores; `Ciudad` no se incluye.

La fila mensual es la unidad del modelo: se le pasan los 12 registros originales, no los seis totales anuales. Así, las predicciones y los valores reales comparados tienen la misma granularidad.

## `ModelEvaluation`

Es un `dataclass` congelado que agrupa la evaluación en un objeto legible:

- `mse`: error cuadrático medio, promedio de los errores de predicción al cuadrado.
- `rmse`: raíz cuadrada del MSE; se expresa en las mismas unidades que `Ventas`.
- `actual`: ventas reales del conjunto de prueba, conservando sus índices y renombrando la serie.
- `predicted`: ventas estimadas por el modelo, con los mismos índices que los valores reales.
- `train_size` y `test_size`: cantidad de registros usados en cada partición.

`frozen=True` evita reasignar campos del resultado después de crearlo; no vuelve inmutables los objetos Series guardados dentro.

## Inicialización de `SalesPredictor`

`test_size` indica la fracción que se reserva para probar; el valor predeterminado es 0.2 (20 %). Se valida que esté estrictamente entre 0 y 1. `random_state=42` fija la semilla del generador aleatorio para que la misma división pueda repetirse.

El predictor crea un `SalesPreprocessor` y un `Pipeline` de Scikit-learn con `LinearRegression`. El pipeline encadena las etapas del estimador; en este caso contiene la regresión y facilita ampliar el preprocesamiento del modelo de forma coherente.

## `evaluate(dataframe)` paso a paso

1. Comprueba que existan las columnas `Año`, `Mes` y `Ventas`. No requiere `Ciudad`.
2. Comprueba que haya al menos dos filas; una no se puede dividir en dos subconjuntos no vacíos.
3. Pide a `SalesPreprocessor` las variables `Año` y `month_number`.
4. Separa el objetivo `target = dataframe["Ventas"]`: es el valor que la regresión debe aprender a estimar.
5. `train_test_split` separa las variables y el objetivo en entrenamiento y prueba, usando el porcentaje y la semilla configurados.
6. `self.model.fit(x_train, y_train)` ajusta la regresión a los datos de entrenamiento.
7. `predict(x_test)` calcula una venta estimada para cada fila de prueba.
8. Convierte las predicciones en una `Series` de Pandas y les asigna los índices de `y_test`. Esto facilita comparar predicción y valor real fila por fila.
9. `mean_squared_error(y_test, predictions)` calcula el MSE. La raíz cuadrada del resultado se guarda como RMSE.
10. Devuelve `ModelEvaluation` con las métricas, series y tamaños.

Con 12 filas y un `test_size` del 20 %, Scikit-learn reserva 3 filas para prueba y usa 9 para entrenamiento.

## Limitaciones importantes

- **No incluye Ciudad:** dos filas de ciudades diferentes con el mismo año y mes tienen las mismas variables predictoras. El modelo no puede diferenciarlas; esto sigue literalmente el requisito confirmado.
- **Pocos datos:** una prueba de solo tres observaciones hace que MSE y RMSE varíen mucho según la partición. Sirven para practicar, no para afirmar que el pronóstico generaliza.
- **Separación aleatoria:** una mezcla aleatoria no simula estrictamente el futuro. Con una serie temporal más grande conviene entrenar con periodos anteriores y evaluar con periodos posteriores.
- **Mes numérico:** enero = 1 y febrero = 2 impone una relación numérica sencilla. Para datos reales se deben estudiar codificaciones temporales y estacionalidad más apropiadas.
- **Datos inválidos:** el preprocesador rechaza meses desconocidos. Valores ausentes o no numéricos de `Ventas` pueden causar un error durante el entrenamiento y deberían tratarse en una etapa explícita si se amplían los datos.

## Por qué `evaluate` hace tanto la división como la evaluación

En este ejercicio didáctico, `evaluate` concentra el procedimiento completo para que la clase de entrada sea fácil de usar. En una aplicación más grande se pueden separar `split`, `fit` y `evaluate`, por ejemplo para reutilizar un modelo ya entrenado o comparar varias estrategias de validación.