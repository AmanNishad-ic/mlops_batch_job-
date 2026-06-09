# MLOps Batch Job

A minimal MLOps-style batch processing pipeline in Python.

## Features

- Reproducibility using config and seed
- Observability using logging and metrics
- Dockerized execution
- CSV batch processing

## Input

Bitcoin OHLCV CSV data

## Generated Features

- price_change
- price_range
- direction

## Run Locally

```bash
pip install -r requirements.txt
python main.py
