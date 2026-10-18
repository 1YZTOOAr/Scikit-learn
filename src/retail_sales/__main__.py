"""Package entry point: python -m retail_sales."""

from .workflow import SalesExercise


def main() -> None:
    """Run the exercise and print its main results."""
    results = SalesExercise().run(show_plot=True)

    print("Missing values by column:")
    print(results.missing_values.to_string())
    print("\nSales statistics:")
    print(results.sales_statistics.to_string())
    print("\nTotal sales by city and year:")
    print(results.annual_sales.to_string(index=False))
    print("\nNormalized sales:")
    print(results.normalized_annual_sales.to_string(index=False))
    print("\nModel evaluation (year and month):")
    print(f"MSE: {results.model_evaluation.mse:.2f}")
    print(f"RMSE: {results.model_evaluation.rmse:.2f}")
    print(
        "Training/test records: "
        f"{results.model_evaluation.train_size}/"
        f"{results.model_evaluation.test_size}"
    )


if __name__ == "__main__":
    main()
