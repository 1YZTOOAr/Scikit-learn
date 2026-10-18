"""Tests for the retail sales exercise."""

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from retail_sales import (
    SalesAnalyzer,
    SalesDataFactory,
    SalesExercise,
    SalesPredictor,
    SalesPreprocessor,
    SalesVisualizer,
)


def test_factory_creates_dataframe_with_all_exercise_records() -> None:
    dataframe = SalesDataFactory().create_dataframe()

    assert dataframe.shape == (12, 4)
    assert dataframe.columns.tolist() == ["Ciudad", "Año", "Mes", "Ventas"]
    assert not dataframe.isna().any().any()
    assert dataframe["Año"].dtype.kind in "iu"
    assert dataframe["Ventas"].dtype.kind in "iu"


def test_analyzer_calculates_city_year_totals() -> None:
    totals = SalesAnalyzer().aggregate_sales(SalesDataFactory().create_dataframe())

    madrid_2021 = totals.query("Ciudad == 'Madrid' and Año == 2021")["Ventas"].item()
    barcelona_2022 = totals.query(
        "Ciudad == 'Barcelona' and Año == 2022"
    )["Ventas"].item()
    assert len(totals) == 6
    assert madrid_2021 == 3200
    assert barcelona_2022 == 4500


def test_preprocessor_normalizes_totals_to_zero_one_without_mutating_input() -> None:
    totals = pd.DataFrame({"Ventas": [10, 20, 30]})

    normalized = SalesPreprocessor().normalize_totals(totals)

    assert normalized["normalized_sales"].tolist() == [0.0, 0.5, 1.0]
    assert "normalized_sales" not in totals


def test_preprocessor_returns_numeric_month_feature_without_city() -> None:
    dataframe = pd.DataFrame(
        {"Ciudad": ["Madrid", "Barcelona"], "Año": [2021, 2022], "Mes": ["Enero", "Febrero"]}
    )

    features = SalesPreprocessor().prepare_model_features(dataframe)

    assert features.columns.tolist() == ["Año", "month_number"]
    assert features["month_number"].tolist() == [1, 2]
    assert "Ciudad" not in features.columns


def test_preprocessor_rejects_unknown_month() -> None:
    dataframe = pd.DataFrame({"Año": [2021], "Mes": ["MesInventado"]})

    with pytest.raises(ValueError, match="Unrecognized months"):
        SalesPreprocessor().prepare_model_features(dataframe)


def test_visualizer_returns_figure_with_labels() -> None:
    totals = SalesAnalyzer().aggregate_sales(SalesDataFactory().create_dataframe())

    figure = SalesVisualizer().plot_annual_sales(totals)

    assert figure.axes[0].get_xlabel() == "City"
    assert figure.axes[0].get_ylabel() == "Sales"
    assert len(figure.axes[0].patches) == 6
    plt.close(figure)


def test_predictor_returns_finite_error_and_reproducible_sizes() -> None:
    dataframe = SalesDataFactory().create_dataframe()

    result = SalesPredictor(random_state=42).evaluate(dataframe)

    assert result.train_size == 9
    assert result.test_size == 3
    assert np.isfinite(result.mse)
    assert np.isfinite(result.rmse)
    assert len(result.predicted) == result.test_size


def test_exercise_runs_and_returns_all_results() -> None:
    results = SalesExercise().run()

    assert len(results.dataframe) == 12
    assert results.missing_values.sum() == 0
    assert len(results.annual_sales) == 6
    assert results.normalized_annual_sales["normalized_sales"].between(0, 1).all()
    assert results.model_evaluation.test_size == 3
