import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.figure(figsize=(10, 6))
    sns.boxplot(df["Attendance"])
    plt.title("Distribution of Attendance")
    plt.xlabel("Attendance")
    plt.ylabel("Percentage")
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()