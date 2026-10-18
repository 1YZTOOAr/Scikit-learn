# `datos.py`: creación de los datos

Código fuente: [`src/ventas_minoristas/datos.py`](../../src/ventas_minoristas/datos.py).

## Propósito

Este módulo contiene los registros ficticios del enunciado y los convierte en un DataFrame de Pandas. Mantiene los datos separados del análisis y del modelo: la clase de este fichero sabe **qué datos** existen, pero no calcula estadísticas ni genera gráficos.

## La clase `SalesDataFactory`

El nombre “factory” (fábrica) describe un objeto cuya responsabilidad es construir otro objeto: en este caso, un DataFrame.

### `_records`

`_records` es una tupla de 12 diccionarios. Cada diccionario representa una observación de ventas con las claves:

- `Ciudad`: ciudad de la tienda (`Madrid`, `Barcelona` o `Valencia`).
- `Año`: año de la observación (`2021` o `2022`), guardado como entero.
- `Mes`: nombre del mes (`Enero` o `Febrero`), guardado como texto.
- `Ventas`: importe ficticio, guardado como entero.

La estructura es equivalente a una tabla: cada diccionario es una fila y todas las filas comparten las mismas columnas. Los valores son los proporcionados en [el enunciado](../ejercicio.md).

El guion bajo inicial indica que `_records` es un detalle interno de la clase. No pretende ser una interfaz para que otros módulos modifiquen los datos.

### `create_dataframe()`

Este método ejecuta `pd.DataFrame(self._records)` y devuelve la tabla de Pandas. Cada llamada crea un DataFrame nuevo, para que los componentes del ejercicio puedan trabajar con él sin que una modificación de una ejecución anterior contamine la siguiente.

El DataFrame tiene 12 filas y 4 columnas. Pandas infiere los tipos: `Año` y `Ventas` son enteros, y `Ciudad` y `Mes` son texto (`object` en las versiones habituales de Pandas).

```python
from ventas_minoristas import SalesDataFactory

df = SalesDataFactory().create_dataframe()
print(df.shape)  # (12, 4)
```

## Por qué no leer un archivo

Los registros son pequeños y están fijados por el ejercicio; por ello se almacenan directamente como datos de ejemplo en Python. Si en el futuro se reciben datos externos o numerosos, se podría añadir una fuente CSV/JSON o base de datos, sin cambiar necesariamente el trabajo de análisis que recibe un DataFrame.