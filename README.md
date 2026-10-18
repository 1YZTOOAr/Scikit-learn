# Análisis y predicción de ventas minoristas

Ejercicio didáctico con **Pandas**, **NumPy**, **Matplotlib** y **Scikit-learn**. El programa crea un DataFrame con ventas ficticias de tres ciudades durante dos años, explora y agrega los datos, visualiza los totales y entrena un modelo de regresión lineal.

## Requisitos

- Python 3.10 o superior.
- `pip` para instalar el proyecto y sus dependencias.

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual si lo deseas y ejecuta:

```powershell
python -m pip install -e ".[test]"
```

Esto instala el paquete en modo editable, sus dependencias de ejecución y `pytest` para las pruebas.

## Ejecutar el ejercicio

```powershell
python -m retail_sales
```

También queda disponible el comando:

```powershell
retail-sales
```

La ejecución muestra los valores ausentes, estadísticas descriptivas, totales por ciudad y año, ventas normalizadas y las métricas MSE y RMSE. En un entorno gráfico, abre también el gráfico de barras.

El modelo usa `Año` y `Mes` como predictores, tal como indica el ejercicio. No utiliza `Ciudad`, por lo que no puede diferenciar predicciones específicas de cada ciudad. Además, el conjunto de solo 12 registros sirve para practicar, no para validar un pronóstico real.

## Pruebas

```powershell
python -m pytest
```

## Documentación

- [Enunciado del ejercicio](docs/exercise.md)
- [Arquitectura del proyecto](docs/architecture.md)
- [Guía detallada de cada fichero fuente](docs/code/index.md)
