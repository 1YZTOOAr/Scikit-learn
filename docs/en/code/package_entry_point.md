# `__main__.py`: running the package

Source file: [`src/retail_sales/__main__.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/__main__.py).

## Purpose

This module is the executable entry point for the package. After installing the project, run it from the repository root with:

```powershell
python -m retail_sales
```

The special filename is `__main__.py`, with two underscores on each side. Python looks for this module when a package is executed with `-m`.

The project also defines a `retail-sales` console command in `pyproject.toml`, which calls the same `main` function.

## Execution sequence

1. Imports `SalesExercise` from `workflow.py`.
2. `main()` creates a `SalesExercise` and calls `run(show_plot=True)`.
3. The workflow returns an `ExerciseResults` object containing outputs from each stage.
4. It prints missing-value counts, descriptive statistics, city/year totals, normalized totals, MSE, RMSE, and training/test sizes.

`to_string()` converts Pandas Series and DataFrames to printable text. `index=False` omits a numeric row index that is not part of the dataset. The `:.2f` format displays errors to two decimal places.

## Guarding the entry point

```python
if __name__ == "__main__":
    main()
```

When run with `python -m retail_sales`, Python sets the module's `__name__` to `"__main__"`, so `main()` runs. If another module imports `retail_sales.__main__`, the function does not run automatically. This separates importing from executing.

## Difference from `workflow.py`

`__main__.py` handles console interaction: it starts the workflow and prints results. `SalesExercise` in `workflow.py` coordinates the computation and returns structured data without deciding how to display it. This lets tests and other programs reuse the workflow.