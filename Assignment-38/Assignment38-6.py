from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DataPath = Path(__file__).with_name("student_performance_ml.csv")

try:
    df = pd.read_csv(DataPath)
except FileNotFoundError:
    print(f"Dataset not found: {DataPath}")
    print("Place student_performance_ml.csv in the Assignment-38 folder.")
else:
    print("StudyHours distribution:")
    print(df["StudyHours"].describe())

    plt.figure(figsize=(7, 5))
    sns.histplot(data=df, x="StudyHours", bins=10, kde=True, color="steelblue")
    plt.title("Distribution of Study Hours")
    plt.xlabel("Study hours per day")
    plt.ylabel("Number of students")
    plt.grid(axis="y", alpha=0.3)
    plt.show()

    print("The histogram shows how many students fall into each StudyHours range.")
    print("The tallest bars identify the most common study-time range.")