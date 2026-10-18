# `data.py`: creating the dataset

Source file: [`src/retail_sales/data.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/data.py).

## Purpose

This module stores the fictional records from the assignment and converts them into a Pandas DataFrame. It keeps data creation separate from analysis and modeling: the class knows **which records** exist, but does not calculate statistics or draw charts.

## `SalesDataFactory`

A factory is an object whose responsibility is to create another object—in this case, a DataFrame.

### `_records`

`_records` is a tuple of 12 dictionaries. Each dictionary is one sales observation with these keys:

- `Ciudad`: store city (`Madrid`, `Barcelona`, or `Valencia`);
- `Año`: observation year (`2021` or `2022`), stored as an integer;
- `Mes`: month name (`Enero` or `Febrero`), stored as text;
- `Ventas`: fictional sales amount, stored as an integer.

The structure is table-like: each dictionary is a row, and all rows share the same columns. The values match the [exercise brief](../exercise.md).

The leading underscore indicates that `_records` is an implementation detail, not a public interface for other modules to modify.

### `create_dataframe()`

The method calls `pd.DataFrame(self._records)` and returns the resulting Pandas table. Each call creates a fresh DataFrame, so changes made during one run do not carry over to another run.

The DataFrame has 12 rows and four columns. Pandas infers integer types for `Año` and `Ventas`, and text/object types for `Ciudad` and `Mes`.

```python
from retail_sales import SalesDataFactory

dataframe = SalesDataFactory().create_dataframe()
print(dataframe.shape)  # (12, 4)
```

## Why the records are not loaded from a file

The exercise has a small, fixed dataset, so the records are included directly in Python. If the project later needs larger or external datasets, a CSV, JSON, or database source could be added while keeping analysis components that accept a DataFrame.