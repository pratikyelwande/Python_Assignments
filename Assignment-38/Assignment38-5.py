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
    grouped = df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean()
    print("Average values by result:")
    print(grouped.rename(index={0: "Fail", 1: "Pass"}).round(2))

    print("\nObservations:")
    print("1. The average StudyHours for passing students is", round(grouped.loc[1, "StudyHours"], 2))
    print("2. The average StudyHours for failing students is", round(grouped.loc[0, "StudyHours"], 2))
    print("3. The average Attendance for passing students is", round(grouped.loc[1, "Attendance"], 2))
    print("4. The average Attendance for failing students is", round(grouped.loc[0, "Attendance"], 2))
    print("5. Higher averages for the passing group suggest that study time and attendance improve passing chances.")