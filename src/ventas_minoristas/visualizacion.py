"""Gráficos del análisis de ventas."""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd


class SalesVisualizer:
    """Genera gráficos y devuelve sus figuras al llamador."""

    def plot_annual_sales(self, totals: pd.DataFrame) -> Figure:
        """Crea un gráfico de barras agrupadas con totales por ciudad y año."""
        required = {"Ciudad", "Año", "Ventas"}
        missing = required.difference(totals.columns)
        if missing:
            raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(missing))}")

        chart_data = totals.pivot(index="Ciudad", columns="Año", values="Ventas")
        figure, axis = plt.subplots(figsize=(9, 5))
        chart_data.plot(kind="bar", ax=axis, subplots=False)
        axis.set_title("Ventas totales por ciudad y año")
        axis.set_xlabel("Ciudad")
        axis.set_ylabel("Ventas")
        axis.legend(title="Año")
        axis.tick_params(axis="x", rotation=0)
        figure.tight_layout()
        return figure
