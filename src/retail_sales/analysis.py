"""Descriptive operations for the sales dataset."""

import pandas as pd


class SalesAnalyzer:
    """Calculate statistics and aggregates without modifying input data."""

    def check_missing_values(self, dataframe: pd.DataFrame) -> pd.Series:
        """Return the number of missing values in each column."""
        return dataframe.isna().sum()

    def describe_sales(self, dataframe: pd.DataFrame) -> pd.Series:
        """Return descriptive statistics for the sales column."""
        self._validate_columns(dataframe, {"Ventas"})
        return dataframe["Ventas"].describe()

    def aggregate_sales(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Calculate total sales for each city and year combination."""
        self._validate_columns(dataframe, {"Ciudad", "Año", "Ventas"})
        totals = (
            dataframe.groupby(["Ciudad", "Año"], sort=True)[["Ventas"]]
            .sum()
            .reset_index()
        )
        return totals

    @staticmethod
    def _validate_columns(dataframe: pd.DataFrame, required: set[str]) -> None:
        missing = required.difference(dataframe.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
