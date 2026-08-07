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
    average_assignments = df.groupby("FinalResult", as_index=False)["AssignmentsCompleted"].mean()
    average_assignments["FinalResult"] = average_assignments["FinalResult"].map({0: "Fail", 1: "Pass"})

    plt.figure(figsize=(7, 5))
    sns.barplot(data=average_assignments, x="FinalResult", y="AssignmentsCompleted", color="teal")
    plt.title("Assignments Completed vs Final Result")
    plt.xlabel("Final result")
    plt.ylabel("Average assignments completed")
    plt.grid(axis="y", alpha=0.3)
    plt.show()

    print("Average assignments completed by result:")
    print(average_assignments)
    print("The taller bar represents the group that completed more assignments on average.")
    print("A higher passing-group average suggests assignments may be associated with success.")