# `preprocesamiento.py`: transformar los datos

Código fuente: [`src/ventas_minoristas/preprocesamiento.py`](../../src/ventas_minoristas/preprocesamiento.py).

## Propósito

`SalesPreprocessor` incluye dos transformaciones distintas: normaliza los totales anuales para el análisis con NumPy y transforma los nombres de los meses a números para el modelo. Separa estas operaciones del análisis de agregados y del entrenamiento.

## Mapa de meses

`_month_numbers` es un diccionario interno que asigna a cada nombre de mes en español un entero: enero = 1, febrero = 2, ..., diciembre = 12. El diccionario permite validar los nombres y produce una variable numérica en el orden natural del calendario.

El conjunto actual solo utiliza enero y febrero. Incluir los doce nombres hace que la transformación se pueda reutilizar si se amplía la tabla. La búsqueda distingue mayúsculas, acentos y espacios: el texto debe coincidir con los nombres del mapa.

## `normalize_totals(totals)`

Este método añade `Ventas_normalizadas` a una **copia** de la tabla de entrada; no modifica la tabla original.

1. Comprueba que exista la columna `Ventas`; si no, lanza `ValueError`.
2. Rechaza una tabla vacía, porque no hay mínimo ni máximo que calcular.
3. Convierte la columna en un arreglo NumPy de tipo flotante.
4. Comprueba con `np.isfinite` que todos los valores sean números finitos, no `NaN` ni infinito.
5. Calcula el mínimo $m$ y el rango $r = \max(x) - m$.
6. Si `r` es distinto de cero, usa la normalización min-max: $x' = (x - m) / r$. Si todos los valores son iguales (`r == 0`), devuelve ceros para evitar dividir entre cero.
7. Copia el DataFrame y añade el arreglo como `Ventas_normalizadas`.

Cuando hay variación, el mínimo queda en 0 y el máximo en 1. Los valores intermedios quedan entre esos extremos. La normalización se aplica a los totales por ciudad y año, no a cada observación mensual.

## `prepare_model_features(dataframe)`

Prepara exactamente las variables predictoras acordadas para el ejercicio: `Año` y `Mes`.

1. Comprueba que existan las columnas `Año` y `Mes`.
2. Copia solo esas dos columnas. `Ciudad` no se usa en el modelo, aunque permanece en el DataFrame original y en el análisis agrupado.
3. Mapea el texto de `Mes` al número correspondiente.
4. Si uno o más meses no están en el mapa (incluidos los ausentes), recopila los valores problemáticos y lanza `ValueError`.
5. Convierte el número de mes a entero y devuelve las columnas `Año` y `Mes_numero`.

El método tampoco cambia el DataFrame que recibe.

## Nota metodológica

Representar los meses como 1 y 2 hace posible entrenar una regresión lineal sencilla, pero los trata como una escala numérica: el modelo supone que la diferencia entre enero y febrero representa un incremento uniforme. Para este ejemplo limitado es una codificación didáctica. En un análisis real se podría usar codificación categórica o variables temporales diseñadas para capturar estacionalidad.