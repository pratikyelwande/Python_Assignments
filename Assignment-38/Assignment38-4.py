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
    result_counts = df["FinalResult"].value_counts().sort_index()
    result_percentages = df["FinalResult"].value_counts(normalize=True).sort_index() * 100

    print("Result counts:")
    print(result_counts.rename(index={0: "Fail", 1: "Pass"}))
    print("\nResult percentages:")
    print(result_percentages.rename(index={0: "Fail", 1: "Pass"}).round(2))

    percentage_difference = abs(result_percentages.get(1, 0) - result_percentages.get(0, 0))
    if percentage_difference <= 10:
        print("\nThe dataset is approximately balanced because the class difference is 10% or less.")
    else:
        print("\nThe dataset is not balanced because the class difference is greater than 10%.")