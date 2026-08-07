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
    plt.figure(figsize=(7, 5))
    sns.boxplot(
        data=df,
        x="FinalResult",
        y="SleepHours",
        hue="FinalResult",
        palette={0: "crimson", 1: "seagreen"},
        legend=False,
    )
    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Final result (0 = Fail, 1 = Pass)")
    plt.ylabel("Sleep hours per day")
    plt.grid(axis="y", alpha=0.3)
    plt.show()

    print("Average SleepHours by result:")
    print(df.groupby("FinalResult")["SleepHours"].mean().rename(index={0: "Fail", 1: "Pass"}))
    print("Sleeping more does not guarantee success because FinalResult depends on multiple factors.")
    print("The plot compares sleep distributions rather than proving that sleep alone causes passing.")