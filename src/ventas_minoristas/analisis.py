"""Operaciones descriptivas sobre las ventas."""

import pandas as pd


class SalesAnalyzer:
    """Calcula estadísticas y agregados sin modificar los datos de entrada."""

    def check_missing_values(self, dataframe: pd.DataFrame) -> pd.Series:
        """Devuelve el número de valores ausentes por columna."""
        return dataframe.isna().sum()

    def describe_sales(self, dataframe: pd.DataFrame) -> pd.Series:
        """Devuelve las estadísticas descriptivas de la columna Ventas."""
        self._validate_columns(dataframe, {"Ventas"})
        return dataframe["Ventas"].describe()

    def aggregate_sales(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Calcula las ventas totales para cada combinación de ciudad y año."""
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
            raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(missing))}")
