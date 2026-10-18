# `analysis.py`: inspection and aggregation

Source file: [`src/retail_sales/analysis.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/analysis.py).

## Purpose

`SalesAnalyzer` performs descriptive calculations with Pandas. It receives a DataFrame and returns results. It does not draw charts, normalize values, or train the model; those tasks belong to other modules.

## `check_missing_values(dataframe)`

`dataframe.isna()` creates a boolean table that marks missing values as `True`. `.sum()` adds those `True` values per column because Pandas treats `True` as 1. The result is a Series containing the number of missing values in each column.

With the supplied records, every count should be zero. This method reports missing values; it does not fill or remove them.

## `describe_sales(dataframe)`

The method first checks that the `Ventas` column exists, then returns `dataframe["Ventas"].describe()`. For a numeric column, Pandas normally returns:

- `count`: number of non-missing values;
- `mean`: arithmetic mean;
- `std`: sample standard deviation;
- `min` and `max`: extremes;
- `25%`, `50%`, and `75%`: quartiles; the 50th percentile is the median.

The result is a Series, not a DataFrame. The input is not modified.

## `aggregate_sales(dataframe)`

This method calculates total sales for each city/year pair:

1. Validates the `Ciudad`, `Año`, and `Ventas` columns.
2. `groupby(["Ciudad", "Año"], sort=True)` forms and sorts groups by the two keys.
3. `[["Ventas"]]` selects the sales column as a DataFrame. The double brackets preserve a two-dimensional DataFrame; selecting with one pair would produce a Series.
4. `.sum()` adds sales within each group.
5. `.reset_index()` turns the grouping keys back into regular columns.

The returned DataFrame has columns `Ciudad`, `Año`, and `Ventas`, and six rows: three cities by two years. For example, Madrid in 2021 totals 3200 and Barcelona in 2022 totals 4500.

## Private validation helper `_validate_columns`

This static method compares the required column set with `dataframe.columns`. If columns are missing, it raises `ValueError` and lists the missing names in sorted order. This gives a clearer failure than a later `KeyError`.

It is static because it does not need instance state. The leading underscore marks it as an internal helper.

## Why the column selection is two-dimensional

`aggregate_sales` promises a `pd.DataFrame`. Selecting `[["Ventas"]]` keeps the grouped object two-dimensional. Selecting one column as a Series can lead Pylance to infer `Series[Any]`, which conflicts with the declared return type. The double brackets make the intent and returned type clear.