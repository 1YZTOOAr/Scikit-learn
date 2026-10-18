# `model.py`: training and evaluating the regression model

Source file: [`src/retail_sales/model.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/model.py).

## Purpose and scope

`SalesPredictor` splits monthly records into training and test sets, fits a linear regression, and calculates prediction error on the held-out records. As required by the exercise, it uses only `Año` and `Mes`; it does not include `Ciudad`.

A monthly row is the unit of observation: the model receives the 12 original records, not the six annual totals. This keeps predictions and actual values at the same granularity.

## `ModelEvaluation`

This frozen dataclass groups the evaluation into a readable object:

- `mse`: mean squared error, the average squared prediction error;
- `rmse`: square root of MSE, expressed in the same units as `Ventas`;
- `actual`: actual sales in the test set, preserving row indices;
- `predicted`: model estimates with the same indices as actual values;
- `train_size` and `test_size`: number of rows in each subset.

`frozen=True` prevents reassigning result attributes, but does not make the contained Pandas Series immutable.

## Initializing `SalesPredictor`

`test_size` is the fraction reserved for testing; it defaults to 0.2 (20%). It must be strictly between 0 and 1. `random_state=42` fixes the random seed so the split is reproducible.

The predictor creates a `SalesPreprocessor` and a Scikit-learn `Pipeline` containing `LinearRegression`. The pipeline provides a consistent place to extend model preprocessing later.

## `evaluate(dataframe)` step by step

1. Checks for `Año`, `Mes`, and `Ventas`. `Ciudad` is not required.
2. Requires at least two rows so both subsets can contain data.
3. Requests `Año` and `month_number` features from `SalesPreprocessor`.
4. Sets `target = dataframe["Ventas"]`, the value the regression learns to estimate.
5. `train_test_split` separates features and target using the configured test fraction and seed.
6. `self.model.fit(x_train, y_train)` trains on the training subset.
7. `predict(x_test)` estimates sales for each test row.
8. Wraps predictions in a Pandas Series with the same indices as `y_test`, allowing row-by-row comparison.
9. `mean_squared_error(y_test, predictions)` calculates MSE; the square root is stored as RMSE.
10. Returns a `ModelEvaluation` containing metrics, values, and subset sizes.

With 12 rows and a 20% test size, Scikit-learn reserves 3 rows for testing and uses 9 for training.

## Important limitations

- **No city feature:** records for different cities with the same year and month have identical predictors, so the model cannot distinguish their city-specific sales. This follows the confirmed assignment scope.
- **Small dataset:** a test set of only three rows makes MSE and RMSE unstable. They are useful for practice, not evidence of general forecasting performance.
- **Random split:** random mixing does not strictly simulate forecasting the future. With more time periods, train on earlier periods and test on later ones.
- **Numeric month:** encoding January as 1 and February as 2 imposes a simple numeric relationship. Real analysis may need categorical encoding or richer time features.
- **Invalid data:** unknown months are rejected. Missing or non-numeric `Ventas` values may cause a training error and would need an explicit handling step in a larger dataset.

## Why `evaluate` handles splitting and evaluation

For this learning exercise, `evaluate` provides the complete process in one easy-to-use method. A larger application could separate splitting, fitting, and evaluation to reuse a trained model or compare validation strategies.