# `__init__.py`: interfaz pública del paquete

Código fuente: [`src/ventas_minoristas/__init__.py`](../../src/ventas_minoristas/__init__.py).

## Para qué sirve

`__init__.py` indica que `ventas_minoristas` es un paquete Python y define qué nombres resulta cómodo importar desde él. No ejecuta el análisis ni crea los datos. Su función es reunir las clases públicas que viven en otros módulos.

Por ejemplo, gracias a este archivo se puede escribir:

```python
from ventas_minoristas import SalesAnalyzer, SalesExercise
```

En vez de importar cada clase por su módulo:

```python
from ventas_minoristas.analisis import SalesAnalyzer
from ventas_minoristas.flujo import SalesExercise
```

## Imports relativos

Las líneas que comienzan con `from .` son imports relativos: el punto significa “desde el paquete actual”. Así, `.analisis` refiere a `analisis.py` dentro de `ventas_minoristas`.

El archivo vuelve accesibles estos nombres:

- `SalesAnalyzer`, desde `analisis.py`.
- `SalesDataFactory`, desde `datos.py`.
- `ExerciseResults` y `SalesExercise`, desde `flujo.py`.
- `ModelEvaluation` y `SalesPredictor`, desde `modelo.py`.
- `SalesPreprocessor`, desde `preprocesamiento.py`.
- `SalesVisualizer`, desde `visualizacion.py`.

## `__all__`

La lista `__all__` declara explícitamente los símbolos que representan la API pública del paquete, por ejemplo al usar `from ventas_minoristas import *`. También sirve como inventario visible de las clases y resultados que otros módulos deberían consumir.

Esto no impide técnicamente importar otros módulos internos; indica la interfaz recomendada y evita exponer detalles privados por accidente.

## Qué no debe colocarse aquí

No se crea un DataFrame, no se entrena un modelo y no se muestra un gráfico en este archivo. Mantenerlo limitado a imports y exportaciones hace que las responsabilidades queden en sus módulos y evita que importar el paquete arranque el ejercicio.