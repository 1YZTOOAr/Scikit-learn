# Exercise: retail sales analysis and prediction

## Context

Artificial intelligence can help retailers optimize operations and make informed decisions. In this exercise, you will use a fictional dataset containing sales from several stores in different cities and years.

The goal is to explore and preprocess the data, calculate useful metrics, visualize results, and build a model to estimate sales.

## Learning objectives

### Data manipulation with Pandas

- Load and explore a dataset.
- Clean the data and handle missing values.
- Group records and calculate statistical metrics.
- Create a bar chart of total sales by city and year.

### NumPy

- Normalize sales for further analysis.

### Prediction with Scikit-learn

- Split the data into training and test sets.
- Train a linear regression model to predict sales.
- Evaluate it with suitable metrics, such as mean squared error (MSE).

## Instructions

### 1. Prepare the environment

Import the libraries required for the exercise: NumPy, Pandas, Matplotlib, and Scikit-learn.

### 2. Create the DataFrame

Create a DataFrame directly from the following records. Each dictionary represents one row. The column names and month values are intentionally kept in Spanish to match the supplied assignment:

```python
import pandas as pd

records = [
    {"Ciudad": "Madrid", "Año": 2021, "Mes": "Enero", "Ventas": 1500},
    {"Ciudad": "Barcelona", "Año": 2021, "Mes": "Enero", "Ventas": 2000},
    {"Ciudad": "Valencia", "Año": 2021, "Mes": "Enero", "Ventas": 1800},
    {"Ciudad": "Madrid", "Año": 2021, "Mes": "Febrero", "Ventas": 1700},
    {"Ciudad": "Barcelona", "Año": 2021, "Mes": "Febrero", "Ventas": 2100},
    {"Ciudad": "Valencia", "Año": 2021, "Mes": "Febrero", "Ventas": 1900},
    {"Ciudad": "Madrid", "Año": 2022, "Mes": "Enero", "Ventas": 1600},
    {"Ciudad": "Barcelona", "Año": 2022, "Mes": "Enero", "Ventas": 2200},
    {"Ciudad": "Valencia", "Año": 2022, "Mes": "Enero", "Ventas": 2000},
    {"Ciudad": "Madrid", "Año": 2022, "Mes": "Febrero", "Ventas": 1800},
    {"Ciudad": "Barcelona", "Año": 2022, "Mes": "Febrero", "Ventas": 2300},
    {"Ciudad": "Valencia", "Año": 2022, "Mes": "Febrero", "Ventas": 2100},
]

dataframe = pd.DataFrame(records)
```

`Año` and `Ventas` are numeric; `Ciudad` and `Mes` are text. Convert `Mes` to a numeric or categorical representation when preparing the model features.

### 3. Explore and clean the data

- Inspect the DataFrame and check for missing values.
- Calculate descriptive statistics for sales, such as the mean and median.

### 4. Group and visualize the data

- Group sales by city and year to calculate annual totals.
- Display the aggregated data in a bar chart.
- Add an appropriate title and axis labels.
- Show the total sales for each city and year.

### 5. Preprocess with NumPy

Normalize the sales totals calculated in the previous step to the range `[0, 1]`.

### 6. Build and evaluate a prediction model

- Convert `Mes` to a numeric representation.
- Use `Año` and `Mes` as predictors of sales.
- Create a linear regression model with Scikit-learn.
- Split the data into a training set (80%) and a test set (20%).
- Evaluate the model with metrics such as MSE.

### 7. Draw conclusions

- Interpret the results of the analysis and prediction model.
- Discuss how the results could help a store manager make decisions.
