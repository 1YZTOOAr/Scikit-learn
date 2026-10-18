"""Punto de entrada del paquete: python -m ventas_minoristas."""

from .flujo import SalesExercise


def main() -> None:
    """Ejecuta el flujo y presenta los resultados principales."""
    results = SalesExercise().run(show_plot=True)

    print("Valores faltantes por columna:")
    print(results.missing_values.to_string())
    print("\nEstadísticas de ventas:")
    print(results.sales_statistics.to_string())
    print("\nVentas totales por ciudad y año:")
    print(results.annual_sales.to_string(index=False))
    print("\nVentas normalizadas:")
    print(results.normalized_annual_sales.to_string(index=False))
    print("\nEvaluación del modelo (Año y Mes):")
    print(f"MSE: {results.model_evaluation.mse:.2f}")
    print(f"RMSE: {results.model_evaluation.rmse:.2f}")
    print(
        "Registros de entrenamiento/prueba: "
        f"{results.model_evaluation.train_size}/"
        f"{results.model_evaluation.test_size}"
    )


if __name__ == "__main__":
    main()
