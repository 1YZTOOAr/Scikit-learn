"""Train and evaluate the linear regression model."""

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from .preprocessing import SalesPreprocessor


@dataclass(frozen=True)
class ModelEvaluation:
    """Evaluation results for the test subset."""

    mse: float
    rmse: float
    actual: pd.Series
    predicted: pd.Series
    train_size: int
    test_size: int


class SalesPredictor:
    """Predict sales using only year and month, as required by the exercise."""

    def __init__(self, test_size: float = 0.2, random_state: int = 42) -> None:
        if not 0 < test_size < 1:
            raise ValueError("test_size must be between 0 and 1")
        self.test_size = test_size
        self.random_state = random_state
        self.preprocessor = SalesPreprocessor()
        self.model = Pipeline([("regression", LinearRegression())])

    def evaluate(self, dataframe: pd.DataFrame) -> ModelEvaluation:
        """Split, train, and evaluate the model with a reproducible seed."""
        required = {"Año", "Mes", "Ventas"}
        missing = required.difference(dataframe.columns)
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        if len(dataframe) < 2:
            raise ValueError("At least two records are required to split the data")

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
            self.model.predict(x_test), index=y_test.index, name="prediction"
        )
        mse = float(mean_squared_error(y_test, predictions))

        return ModelEvaluation(
            mse=mse,
            rmse=mse**0.5,
            actual=y_test.rename("actual_sales"),
            predicted=predictions,
            train_size=len(x_train),
            test_size=len(x_test),
        )
