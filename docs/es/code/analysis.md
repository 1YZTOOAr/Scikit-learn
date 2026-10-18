# `analysis.py`: inspección y agregación

Código fuente: [`src/retail_sales/analysis.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/analysis.py).

## Propósito

`SalesAnalyzer` realiza cálculos descriptivos con Pandas. Recibe un DataFrame y devuelve resultados. No genera gráficos, no normaliza los datos y no entrena el modelo; esas responsabilidades pertenecen a otros módulos.

## `check_missing_values(dataframe)`

`dataframe.isna()` crea una tabla booleana que marca `True` donde falta un valor. `.sum()` suma los `True` por columna, ya que en Pandas `True` cuenta como 1. El resultado es una `Series` con el número de valores ausentes de cada columna.

Con los datos actuales, cada columna debe tener cero valores faltantes. El método no rellena ni elimina valores: solo informa, de forma que el llamador decida qué hacer si los hubiera.

## `describe_sales(dataframe)`

Primero valida que exista la columna `Ventas`, luego devuelve `dataframe["Ventas"].describe()`. Para una columna numérica, Pandas calcula normalmente:

- `count`: número de valores no ausentes;
- `mean`: media aritmética;
- `std`: desviación estándar muestral;
- `min`, `max`: extremos;
- `25%`, `50%`, `75%`: cuartiles; el 50 % es la mediana.

El resultado es una `Series`, no un DataFrame. Este método no cambia los datos originales.

## `aggregate_sales(dataframe)`

Este método produce el total de ventas para cada combinación de ciudad y año:

1. Valida las columnas `Ciudad`, `Año` y `Ventas`.
2. `groupby(["Ciudad", "Año"], sort=True)` crea grupos para las combinaciones de esas dos columnas y los ordena por sus claves.
3. `[["Ventas"]]` selecciona la columna como DataFrame. Los dobles corchetes son importantes: seleccionar la columna con un solo par de corchetes produce una Series; con dos pares se conserva una tabla bidimensional.
4. `.sum()` suma las ventas dentro de cada grupo.
5. `.reset_index()` convierte las claves del grupo otra vez en columnas normales del resultado.

El resultado tiene las columnas `Ciudad`, `Año`, `Ventas` y seis filas: tres ciudades multiplicadas por dos años. Con los registros actuales, por ejemplo, Madrid en 2021 suma 3200 y Barcelona en 2022 suma 4500.

## Validación privada `_validate_columns`

La función estática compara el conjunto `required` (columnas requeridas) con los nombres presentes en `dataframe.columns`. Si faltan columnas, calcula la diferencia y lanza `ValueError` con los nombres faltantes ordenados. Así, en vez de fallar más tarde con un `KeyError` menos explicativo, el error indica qué entrada no cumple el contrato.

Es estática porque no necesita consultar ni modificar el estado de una instancia. Es privada por convención (`_` inicial) porque solo se usa como ayuda interna del analizador.

## Por qué la selección es bidimensional

El tipo que promete `aggregate_sales` es `pd.DataFrame`. Seleccionar la columna como una lista de columnas (`[["Ventas"]]`) mantiene la agrupación como DataFrame. Si se selecciona como una sola columna, el resultado es una Series y Pylance puede inferirla como `Series[Any]`, incompatible con el tipo de retorno. Por eso se conservan los dobles corchetes.