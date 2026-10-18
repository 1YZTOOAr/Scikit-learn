# `__init__.py`: interfaz pública del paquete

Código fuente: [`src/retail_sales/__init__.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/__init__.py).

## Para qué sirve

`__init__.py` indica que `retail_sales` es un paquete Python y define qué nombres resulta cómodo importar desde él. No ejecuta el análisis ni crea los datos. Su función es reunir las clases públicas que viven en otros módulos.

Por ejemplo, gracias a este archivo se puede escribir:

```python
from retail_sales import SalesAnalyzer, SalesExercise
```

En vez de importar cada clase por su módulo:

```python
from retail_sales.analysis import SalesAnalyzer
from retail_sales.workflow import SalesExercise
```

## Imports relativos

Las líneas que comienzan con `from .` son imports relativos: el punto significa “desde el paquete actual”. Así, `.analysis` refiere a `analysis.py` dentro de `retail_sales`.

El archivo vuelve accesibles estos nombres:

- `SalesAnalyzer`, desde `analysis.py`.
- `SalesDataFactory`, desde `data.py`.
- `ExerciseResults` y `SalesExercise`, desde `workflow.py`.
- `ModelEvaluation` y `SalesPredictor`, desde `model.py`.
- `SalesPreprocessor`, desde `preprocessing.py`.
- `SalesVisualizer`, desde `visualization.py`.

## `__all__`

La lista `__all__` declara explícitamente los símbolos que representan la API pública del paquete, por ejemplo al usar `from retail_sales import *`. También sirve como inventario visible de las clases y resultados que otros módulos deberían consumir.

Esto no impide técnicamente importar otros módulos internos; indica la interfaz recomendada y evita exponer detalles privados por accidente.

## Qué no debe colocarse aquí

No se crea un DataFrame, no se entrena un modelo y no se muestra un gráfico en este archivo. Mantenerlo limitado a imports y exportaciones hace que las responsabilidades queden en sus módulos y evita que importar el paquete arranque el ejercicio.