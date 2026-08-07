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
    print("Average StudyHours:", df["StudyHours"].mean())
    print("Average Attendance:", df["Attendance"].mean())
    print("Maximum PreviousScore:", df["PreviousScore"].max())
    print("Minimum SleepHours:", df["SleepHours"].min())