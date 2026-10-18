# `visualization.py`: sales chart

Source file: [`src/retail_sales/visualization.py`](https://github.com/1YZTOOAr/Scikit-learn/blob/main/src/retail_sales/visualization.py).

## Purpose

`SalesVisualizer` turns aggregated data into a bar chart. It receives totals from `SalesAnalyzer`, does not aggregate or change the input DataFrame, and returns a Matplotlib figure so another component can decide when to show or close it.

## `plot_annual_sales(totals)` step by step

1. Checks that `Ciudad`, `Año`, and `Ventas` exist. If a column is missing, raises `ValueError` listing the required columns.
2. `pivot(index="Ciudad", columns="Año", values="Ventas")` reshapes the data: cities become rows, years become columns, and sales are the values. `pivot` expects one value per city/year pair, so it receives already aggregated totals.
3. `plt.subplots(figsize=(9, 5))` creates a 9-by-5-inch figure and an axis.
4. `chart_data.plot(kind="bar", ax=axis, subplots=False)` draws each year as a series of grouped bars on the same axis, making year-to-year comparison within each city easy. `subplots=False` is explicit so Pandas uses a single panel and the call satisfies the type signature used by Pylance.
5. Sets the title, axis labels, and legend title.
6. Sets horizontal tick labels to zero-degree rotation and uses `figure.tight_layout()` to prevent clipping.
7. Returns a `Figure` imported from `matplotlib.figure`. It is not annotated as `plt.Figure` because `Figure` is not exported from `matplotlib.pyplot`.
8. Does not call `plt.show()`. This lets tests inspect the figure and lets the workflow control when it is displayed.

## Why the figure is not shown here

Visualization and presentation are separate responsibilities. The caller may display, save, or close the figure. `SalesExercise.run(show_plot=...)` decides whether to display it interactively or close it.

## One chart or several subplots

The `subplots` option controls how the pivoted DataFrame columns (years) are displayed:

- With `subplots=False`, all years appear on the same axis as grouped bars for each city. This is the implementation because it makes direct year comparisons within each city easy.
- With `subplots=True`, Pandas creates one axis per year. Each panel makes city comparisons for that year clear, but comparing a city's change across years is less direct.

Subplots change the visual layout; they do not add data or perform another analysis. For three cities and two years, one grouped chart is more compact and comparative.

## Input errors

The method validates columns before pivoting. If the input contains multiple rows for one city/year pair, `pivot` cannot select a single value; the method expects the aggregated output of `aggregate_sales`.