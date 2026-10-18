# `__main__.py`: ejecutar el paquete

Código fuente: [`src/retail_sales/__main__.py`](../../src/retail_sales/__main__.py).

## Función del fichero

Este módulo es el punto de entrada ejecutable del paquete. Después de instalar el proyecto, se puede iniciar desde la raíz del repositorio con:

```powershell
python -m retail_sales
```

El nombre especial correcto es `__main__.py`, con dos guiones bajos al principio y al final. Python busca este fichero cuando se ejecuta el paquete con `-m`.

El proyecto también define en `pyproject.toml` el comando de consola `retail-sales`, que llama a la misma función `main`.

## Secuencia de ejecución

1. Importa `SalesExercise` desde el módulo de coordinación `workflow.py`.
2. `main()` crea una instancia de `SalesExercise` y llama a `run(show_plot=True)`.
3. El flujo devuelve un objeto `ExerciseResults` que contiene los resultados de cada etapa.
4. Imprime en la consola:
   - valores ausentes por columna;
   - estadísticas descriptivas de ventas;
   - totales por ciudad y año;
   - totales normalizados;
   - MSE, RMSE y cantidad de registros de entrenamiento y prueba.

`to_string()` transforma las series o tablas de Pandas en texto imprimible; en las tablas se usa `index=False` para no mostrar un índice numérico que no es un dato del ejercicio. Los formatos `:.2f` muestran los errores con dos decimales.

## Protección del punto de entrada

```python
if __name__ == "__main__":
    main()
```

Al ejecutar `python -m retail_sales`, Python establece `__name__` del módulo ejecutado como `"__main__"`, por lo que se llama a `main()`. Si otro módulo importa `retail_sales.__main__`, la función no se ejecuta automáticamente. Este patrón separa la importación de la ejecución.

## Diferencia entre este módulo y `workflow.py`

`__main__.py` se ocupa de la interacción de consola: inicia el trabajo y presenta los resultados. `SalesExercise` en `workflow.py` organiza el proceso y devuelve datos estructurados, sin decidir cómo se imprimen. Esta separación hace que el flujo pueda reutilizarse desde pruebas u otro programa.