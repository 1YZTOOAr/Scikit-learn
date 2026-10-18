"""Sales analysis charts."""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd


class SalesVisualizer:
    """Create charts and return their figures to the caller."""

    def plot_annual_sales(self, totals: pd.DataFrame) -> Figure:
        """Create a grouped bar chart of annual totals for each city."""
        required = {"Ciudad", "Año", "Ventas"}
        missing = required.difference(totals.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        chart_data = totals.pivot(index="Ciudad", columns="Año", values="Ventas")
        figure, axis = plt.subplots(figsize=(9, 5))
        chart_data.plot(kind="bar", ax=axis, subplots=False)
        axis.set_title("Total sales by city and year")
        axis.set_xlabel("City")
        axis.set_ylabel("Sales")
        axis.legend(title="Year")
        axis.tick_params(axis="x", rotation=0)
        figure.tight_layout()
        return figure
