# Guía detallada del código fuente

Esta carpeta explica, fichero por fichero, la lógica del paquete implementado en [`src/retail_sales/`](https://github.com/1YZTOOAr/Scikit-learn/tree/main/src/retail_sales/). Está pensada como material de apoyo para seguir el ejercicio en clase.

## Documentación por fichero

- [`__init__.py`: interfaz pública del paquete](./package_api.md)
- [`__main__.py`: ejecución del programa](./package_entry_point.md)
- [`data.py`: construcción del DataFrame](./data.md)
- [`analysis.py`: inspección y agregación](./analysis.md)
- [`preprocessing.py`: normalización y preparación de variables](./preprocessing.md)
- [`visualization.py`: gráfico de barras](./visualization.md)
- [`model.py`: regresión lineal y evaluación](./model.md)
- [`workflow.py`: coordinación de todo el ejercicio](./workflow.md)

## Orden recomendado de lectura

1. [`data.md`](./data.md), para comprender de dónde salen los datos.
2. [`analysis.md`](./analysis.md), [`preprocessing.md`](./preprocessing.md) y [`visualization.md`](./visualization.md), para seguir las operaciones sobre el DataFrame.
3. [`model.md`](./model.md), para entender entrenamiento y evaluación.
4. [`workflow.md`](./workflow.md) y [`package_entry_point.md`](./package_entry_point.md), para ver cómo se conectan las piezas y se ejecuta el programa.
5. [`package_api.md`](./package_api.md), para conocer la interfaz de importación del paquete.

Para leer primero los requisitos, consulta el [enunciado del ejercicio](../exercise.md) y la [arquitectura general](../architecture.md).