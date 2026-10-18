"""Numeric transformations for analysis and modeling."""

import numpy as np
import pandas as pd


class SalesPreprocessor:
    """Normalize aggregates and encode month names for the model."""

    _month_to_number = {
        "Enero": 1,
        "Febrero": 2,
        "Marzo": 3,
        "Abril": 4,
        "Mayo": 5,
        "Junio": 6,
        "Julio": 7,
        "Agosto": 8,
        "Septiembre": 9,
        "Octubre": 10,
        "Noviembre": 11,
        "Diciembre": 12,
    }

    def normalize_totals(self, totals: pd.DataFrame) -> pd.DataFrame:
        """Add normalized_sales in [0, 1] without modifying the input."""
        if "Ventas" not in totals.columns:
            raise ValueError("Missing required column: Ventas")
        if totals.empty:
            raise ValueError("Cannot normalize sales without any records")

        values = totals["Ventas"].to_numpy(dtype=float)
        if not np.isfinite(values).all():
            raise ValueError("Sales values must be finite numbers")

        minimum = values.min()
        span = values.max() - minimum
        normalized = np.zeros_like(values) if span == 0 else (values - minimum) / span

        result = totals.copy()
        result["normalized_sales"] = normalized
        return result

    def prepare_model_features(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Return year and month_number features, without using city."""
        required = {"Año", "Mes"}
        missing = required.difference(dataframe.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        result = dataframe[["Año", "Mes"]].copy()
        month_number = result["Mes"].map(self._month_to_number)
        if month_number.isna().any():
            invalid_months = sorted(result.loc[month_number.isna(), "Mes"].astype(str).unique())
            raise ValueError(f"Unrecognized months: {', '.join(invalid_months)}")
        result["month_number"] = month_number.astype(int)
        return result[["Año", "month_number"]]
