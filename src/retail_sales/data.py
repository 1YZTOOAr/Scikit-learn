"""Build the fixed dataset used in the exercise."""

import pandas as pd


class SalesDataFactory:
    """Create the sales DataFrame defined by the exercise."""

    _records = (
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
    )

    def create_dataframe(self) -> pd.DataFrame:
        """Return a new DataFrame containing the exercise records."""
        return pd.DataFrame(self._records)
