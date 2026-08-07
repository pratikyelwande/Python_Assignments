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
    print("Attendance summary:")
    print(df["Attendance"].describe())

    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df["Attendance"], color="darkorange")
    plt.title("Boxplot of Attendance")
    plt.xlabel("Attendance percentage")
    plt.grid(axis="x", alpha=0.3)
    plt.show()

    first_quartile = df["Attendance"].quantile(0.25)
    third_quartile = df["Attendance"].quantile(0.75)
    interquartile_range = third_quartile - first_quartile
    lower_limit = first_quartile - 1.5 * interquartile_range
    upper_limit = third_quartile + 1.5 * interquartile_range
    outliers = df[(df["Attendance"] < lower_limit) | (df["Attendance"] > upper_limit)]
    print("Number of Attendance outliers:", len(outliers))
    print("Outliers are values outside 1.5 times the interquartile range.")