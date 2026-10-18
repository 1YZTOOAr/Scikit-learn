# Source-code guide

This section explains the logic of each module in [`src/retail_sales/`](https://github.com/1YZTOOAr/Scikit-learn/tree/main/src/retail_sales/). It is intended as a learning companion to the exercise.

## Module guides

- [`__init__.py`: package public API](package_api.md)
- [`__main__.py`: package entry point](package_entry_point.md)
- [`data.py`: DataFrame creation](data.md)
- [`analysis.py`: inspection and aggregation](analysis.md)
- [`preprocessing.py`: normalization and feature preparation](preprocessing.md)
- [`visualization.py`: bar chart](visualization.md)
- [`model.py`: linear regression and evaluation](model.md)
- [`workflow.py`: coordinating the exercise](workflow.md)

## Suggested reading order

1. Read [data.py](data.md) to understand how records become a DataFrame.
2. Follow [analysis.py](analysis.md), [preprocessing.py](preprocessing.md), and [visualization.py](visualization.md) to see how the data is inspected and transformed.
3. Read [model.py](model.md) to understand training and evaluation.
4. Finish with [workflow.py](workflow.md), [__main__.py](package_entry_point.md), and [__init__.py](package_api.md) to see how the modules fit together.

For the requirements and overall design, see the [exercise brief](../exercise.md) and [architecture](../architecture.md).