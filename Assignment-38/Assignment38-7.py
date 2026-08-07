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
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="StudyHours",
        y="PreviousScore",
        hue="FinalResult",
        palette={0: "crimson", 1: "seagreen"},
        hue_order=[0, 1],
    )
    plt.title("Study Hours vs Previous Score")
    plt.xlabel("Study hours per day")
    plt.ylabel("Previous examination score")
    plt.legend(title="Final Result", labels=["Fail", "Pass"])
    plt.grid(alpha=0.3)
    plt.show()