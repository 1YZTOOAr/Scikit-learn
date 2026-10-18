# `visualization.py`: gráfico de ventas

Código fuente: [`src/retail_sales/visualization.py`](../../src/retail_sales/visualization.py).

## Propósito

`SalesVisualizer` convierte la tabla agregada en un gráfico de barras. Recibe los totales calculados por `SalesAnalyzer`; no agrega ni transforma el DataFrame original y devuelve una figura de Matplotlib para que otro componente decida cuándo mostrarla o cerrarla.

## `plot_annual_sales(totals)` paso a paso

1. Comprueba que existan las columnas `Ciudad`, `Año` y `Ventas`. Si falta alguna, lanza `ValueError` con los nombres requeridos.
2. `pivot(index="Ciudad", columns="Año", values="Ventas")` reorganiza la tabla: las ciudades quedan como filas, los años como columnas y las ventas como valores. `pivot` espera un solo valor por ciudad/año; por eso debe recibir el resultado ya agregado.
3. `plt.subplots(figsize=(9, 5))` crea la figura y un eje donde dibujar, con tamaño de 9 por 5 pulgadas.
4. `chart_data.plot(kind="bar", ax=axis, subplots=False)` dibuja las series de años en el mismo eje: cada ciudad tiene barras agrupadas que permiten comparar los años de un vistazo. Se indica `subplots=False` explícitamente para que Pandas use un solo panel y para satisfacer la firma de tipos que utiliza Pylance.
5. Configura el título, los rótulos de los ejes y la leyenda titulada `Año`.
6. Fija la rotación de las etiquetas del eje horizontal a cero grados y ajusta el espacio con `figure.tight_layout()`.
7. Devuelve un objeto `Figure`, importado desde `matplotlib.figure`. No se anota como `plt.Figure`, porque `Figure` no está exportada desde `matplotlib.pyplot`.
8. El método no llama a `plt.show()`, lo que permite que las pruebas inspeccionen el resultado y que el orquestador controle el momento de presentarlo.

## Por qué no se muestra directamente aquí

La visualización y la presentación son responsabilidades diferentes. Al devolver la figura, quien llama decide si la abre en una ventana, la guarda en un fichero o la cierra. En el flujo del ejercicio, `SalesExercise.run(show_plot=...)` decide mostrarla en modo interactivo y cerrarla cuando no se solicita.

## Un solo gráfico o varios subgráficos

La opción `subplots` decide cómo mostrar las columnas del DataFrame pivotado (en este caso, los años):

- Con `subplots=False`, todos los años se muestran en el mismo eje, como grupos de barras por ciudad. Es la opción implementada porque facilita comparar directamente los años dentro de cada ciudad.
- Con `subplots=True`, Pandas crea un eje independiente por año. Cada panel permite comparar las ciudades de ese año, pero resulta menos directo comparar el cambio entre años para una ciudad concreta.

Los subgráficos cambian la disposición visual, no añaden información ni realizan un análisis adicional. Para los tres municipios y dos años de este ejercicio, el gráfico agrupado en un solo eje es más compacto y comparativo.

## Errores de entrada

Si falta una columna, la validación da un error explícito antes de intentar el pivote. Si la tabla contiene más de una fila para la misma ciudad y año, `pivot` no puede determinar un único valor; el contrato del método es recibir los resultados agregados de `aggregate_sales`.