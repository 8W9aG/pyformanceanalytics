#!/bin/sh

echo "Formatting..."
echo "--- Ruff ---"
ruff format pyformanceanalytics
echo "--- isort ---"
isort pyformanceanalytics

echo "Checking..."
echo "--- Flake8 ---"
flake8 pyformanceanalytics
echo "--- pylint ---"
pylint pyformanceanalytics
echo "--- mypy ---"
mypy pyformanceanalytics
echo "--- Ruff ---"
ruff check pyformanceanalytics
echo "--- pyright ---"
pyright pyformanceanalytics
