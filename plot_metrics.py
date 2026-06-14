# Updated code to handle empty input
import pandas as pd

def plot_metrics(data):
    if data.empty:
        raise ValueError("Input data is empty")
    # rest of the plotting logic