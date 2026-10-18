"""Coordinate the complete exercise workflow."""

from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd

from .analysis import SalesAnalyzer
from .data import SalesDataFactory
from .model import ModelEvaluation, SalesPredictor
from .preprocessing import SalesPreprocessor
from .visualization import SalesVisualizer


@dataclass(frozen=True)
class ExerciseResults:
    """Results produced by each stage of the exercise."""

    dataframe: pd.DataFrame
    missing_values: pd.Series
    sales_statistics: pd.Series
    annual_sales: pd.DataFrame
    normalized_annual_sales: pd.DataFrame
    model_evaluation: ModelEvaluation


class SalesExercise:
    """Orchestrate sales data creation, analysis, visualization, and prediction."""

    def __init__(
        self,
        data_factory: SalesDataFactory | None = None,
        analyzer: SalesAnalyzer | None = None,
        preprocessor: SalesPreprocessor | None = None,
        visualizer: SalesVisualizer | None = None,
        predictor: SalesPredictor | None = None,
    ) -> None:
        self.data_factory = data_factory or SalesDataFactory()
        self.analyzer = analyzer or SalesAnalyzer()
        self.preprocessor = preprocessor or SalesPreprocessor()
        self.visualizer = visualizer or SalesVisualizer()
        self.predictor = predictor or SalesPredictor()

    def run(self, show_plot: bool = False) -> ExerciseResults:
        """Run each stage and return its results; displaying the plot is optional."""
        dataframe = self.data_factory.create_dataframe()
        missing_values = self.analyzer.check_missing_values(dataframe)
        sales_statistics = self.analyzer.describe_sales(dataframe)
        annual_sales = self.analyzer.aggregate_sales(dataframe)
        normalized_annual_sales = self.preprocessor.normalize_totals(annual_sales)
        figure = self.visualizer.plot_annual_sales(annual_sales)
        model_evaluation = self.predictor.evaluate(dataframe)

        if show_plot and figure.canvas.required_interactive_framework is not None:
            plt.show()
        else:
            plt.close(figure)

        return ExerciseResults(
            dataframe=dataframe,
            missing_values=missing_values,
            sales_statistics=sales_statistics,
            annual_sales=annual_sales,
            normalized_annual_sales=normalized_annual_sales,
            model_evaluation=model_evaluation,
        )
