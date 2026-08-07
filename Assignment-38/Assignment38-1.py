from pathlib import Path

import pandas as pd


Border = "-" * 30
DataPath = Path(__file__).with_name("student_performance_ml.csv")

try:
    df = pd.read_csv(DataPath)
except FileNotFoundError:
    print(f"Dataset not found: {DataPath}")
    print("Place student_performance_ml.csv in the Assignment-38 folder.")
else:
    print("First 5 records:")
    print(df.head())

    print("\nLast 5 records:")
    print(df.tail())

    print("\nTotal rows and columns:", df.shape)
    print("Column names:", list(df.columns))
    print("\nData types:")
    print(df.dtypes)