# `preprocessing.py`: transforming data

Source file: [`src/retail_sales/preprocessing.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/preprocessing.py).

## Purpose

`SalesPreprocessor` contains two transformations: it normalizes annual totals for descriptive analysis using NumPy and converts month names to numbers for the model. These operations are separate from aggregation and model training.

## Month mapping

`_month_to_number` is an internal dictionary mapping each Spanish month name to an integer: January (`Enero`) = 1, February (`Febrero`) = 2, through December (`Diciembre`) = 12. The mapping validates month names and places them in calendar order.

The supplied data uses only January and February. Including all months makes the transformation reusable if the dataset grows. Matching is case-sensitive and requires the Spanish month name to match the dictionary exactly.

## `normalize_totals(totals)`

This method adds `normalized_sales` to a **copy** of the input table; the original is not changed.

1. Checks that the `Ventas` column exists; otherwise raises `ValueError`.
2. Rejects an empty table because it has no minimum or maximum.
3. Converts the column to a floating-point NumPy array.
4. Uses `np.isfinite` to reject missing or infinite values.
5. Calculates the minimum $m$ and range $r = \max(x) - m$.
6. If `r` is nonzero, applies min-max normalization: $x' = (x - m) / r$. If all values are identical (`r == 0`), it returns zeros to avoid division by zero.
7. Copies the DataFrame and adds the array as `normalized_sales`.

When values vary, the minimum maps to 0 and maximum to 1; values in between remain in that interval. Normalization is applied to city/year totals, not individual monthly observations.

## `prepare_model_features(dataframe)`

This method prepares the exact predictors selected for the exercise: `Año` and `Mes`.

1. Checks that the `Año` and `Mes` columns exist.
2. Copies only those columns. `Ciudad` is not used by the model, but remains in the original DataFrame and grouped analysis.
3. Maps each month name to its number.
4. If any month is unknown or missing, collects the invalid values and raises `ValueError`.
5. Converts the month number to an integer and returns `Año` and `month_number`.

The input DataFrame is not modified.

## Methodological note

Representing months as 1 and 2 lets a simple linear regression use them, but treats months as a numeric scale. The model assumes a uniform step from January to February. This is suitable for the limited exercise; real analysis may require categorical encoding or richer time features to represent seasonality.