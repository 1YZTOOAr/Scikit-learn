"""Entrenamiento y evaluación del modelo de regresión lineal."""

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from .preprocesamiento import SalesPreprocessor


@dataclass(frozen=True)
class ModelEvaluation:
    """Resultados de evaluación sobre el subconjunto de prueba."""

    mse: float
    rmse: float
    actual: pd.Series
    predicted: pd.Series
    train_size: int
    test_size: int


class SalesPredictor:
    """Predice ventas usando únicamente Año y Mes, como pide el enunciado."""

    def __init__(self, test_size: float = 0.2, random_state: int = 42) -> None:
        if not 0 < test_size < 1:
            raise ValueError("test_size debe estar entre 0 y 1")
        self.test_size = test_size
        self.random_state = random_state
        self.preprocessor = SalesPreprocessor()
        self.model = Pipeline([("regression", LinearRegression())])

    def evaluate(self, dataframe: pd.DataFrame) -> ModelEvaluation:
        """Divide, entrena y evalúa el modelo con una semilla reproducible."""
        required = {"Año", "Mes", "Ventas"}
        missing = required.difference(dataframe.columns)
        if missing:
            raise ValueError(f"Faltan columnas requeridas: {', '.join(sorted(missing))}")
        if len(dataframe) < 2:
            raise ValueError("Se necesitan al menos dos registros para dividir los datos")

        features = self.preprocessor.prepare_model_features(dataframe)
        target = dataframe["Ventas"]
        x_train, x_test, y_train, y_test = train_test_split(
            features,
            target,
            test_size=self.test_size,
            random_state=self.random_state,
        )
        self.model.fit(x_train, y_train)
        predictions = pd.Series(
            self.model.predict(x_test), index=y_test.index, name="Prediccion"
        )
        mse = float(mean_squared_error(y_test, predictions))

        return ModelEvaluation(
            mse=mse,
            rmse=mse**0.5,
            actual=y_test.rename("Ventas_reales"),
            predicted=predictions,
            train_size=len(x_train),
            test_size=len(x_test),
        )
