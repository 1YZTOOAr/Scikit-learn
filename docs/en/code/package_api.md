# `__init__.py`: the package public API

Source file: [`src/retail_sales/__init__.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/__init__.py).

## Purpose

`__init__.py` marks `retail_sales` as a Python package and gathers the names that are convenient to import from the package. It does not run the analysis or create data; it exposes classes defined in other modules.

For example, this file allows:

```python
from retail_sales import SalesAnalyzer, SalesExercise
```

Instead of importing each class from its module:

```python
from retail_sales.analysis import SalesAnalyzer
from retail_sales.workflow import SalesExercise
```

## Relative imports

Imports beginning with `from .` are relative imports. The dot means “from the current package.” For example, `.analysis` refers to `analysis.py` inside `retail_sales`.

The package exposes:

- `SalesAnalyzer` from `analysis.py`;
- `SalesDataFactory` from `data.py`;
- `ExerciseResults` and `SalesExercise` from `workflow.py`;
- `ModelEvaluation` and `SalesPredictor` from `model.py`;
- `SalesPreprocessor` from `preprocessing.py`;
- `SalesVisualizer` from `visualization.py`.

## `__all__`

The `__all__` list explicitly names the package's public symbols, for example when a caller uses `from retail_sales import *`. It is also a concise inventory of the classes and result objects intended for consumers.

It does not technically prevent importing internal modules; it documents the recommended public interface and helps avoid exposing implementation details accidentally.

## What does not belong here

This module should not create a DataFrame, train a model, or show a chart. Keeping it limited to imports and exports ensures each task stays in its own module and importing the package does not start the exercise.