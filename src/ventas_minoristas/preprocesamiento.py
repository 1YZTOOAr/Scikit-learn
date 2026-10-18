"""Transformaciones numéricas para el análisis y el modelo."""

import numpy as np
import pandas as pd


class SalesPreprocessor:
    """Normaliza agregados y codifica meses para el modelo."""

    _month_numbers = {
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
        """Añade Ventas_normalizadas en el rango [0, 1] sin alterar el original."""
        if "Ventas" not in totals.columns:
            raise ValueError("Falta la columna requerida: Ventas")
        if totals.empty:
            raise ValueError("No se pueden normalizar ventas sin registros")

        values = totals["Ventas"].to_numpy(dtype=float)
        if not np.isfinite(values).all():
            raise ValueError("Las ventas deben ser valores numéricos finitos")

        minimum = values.min()
        span = values.max() - minimum
        normalized = np.zeros_like(values) if span == 0 else (values - minimum) / span

        result = totals.copy()
        result["Ventas_normalizadas"] = normalized
        return result

    def prepare_model_features(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Devuelve Año y Mes_numero, sin usar Ciudad como predictor."""
        required = {"Año", "Mes"}
        missing = required.difference(dataframe.columns)
        if missing:
            raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(missing))}")

        result = dataframe[["Año", "Mes"]].copy()
        month_number = result["Mes"].map(self._month_numbers)
        if month_number.isna().any():
            invalid_months = sorted(result.loc[month_number.isna(), "Mes"].astype(str).unique())
            raise ValueError(f"Meses no reconocidos: {', '.join(invalid_months)}")
        result["Mes_numero"] = month_number.astype(int)
        return result[["Año", "Mes_numero"]]
