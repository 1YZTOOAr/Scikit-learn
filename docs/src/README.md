# Guía detallada del código fuente

Esta carpeta explica, fichero por fichero, la lógica del paquete implementado en [`src/ventas_minoristas/`](../../src/ventas_minoristas/). Está pensada como material de apoyo para seguir el ejercicio en clase.

## Documentación por fichero

- [`__init__.py`: interfaz pública del paquete](./init.md)
- [`__main__.py`: ejecución del programa](./main.md)
- [`datos.py`: construcción del DataFrame](./datos.md)
- [`analisis.py`: inspección y agregación](./analisis.md)
- [`preprocesamiento.py`: normalización y preparación de variables](./preprocesamiento.md)
- [`visualizacion.py`: gráfico de barras](./visualizacion.md)
- [`modelo.py`: regresión lineal y evaluación](./modelo.md)
- [`flujo.py`: coordinación de todo el ejercicio](./flujo.md)

## Orden recomendado de lectura

1. [`datos.md`](./datos.md), para comprender de dónde salen los datos.
2. [`analisis.md`](./analisis.md), [`preprocesamiento.md`](./preprocesamiento.md) y [`visualizacion.md`](./visualizacion.md), para seguir las operaciones sobre el DataFrame.
3. [`modelo.md`](./modelo.md), para entender entrenamiento y evaluación.
4. [`flujo.md`](./flujo.md) y [`main.md`](./main.md), para ver cómo se conectan las piezas y se ejecuta el programa.
5. [`init.md`](./init.md), para conocer la interfaz de importación del paquete.

Para leer primero los requisitos, consulta el [enunciado del ejercicio](../ejercicio.md) y la [arquitectura general](../arquitectura_ejercicio.md).