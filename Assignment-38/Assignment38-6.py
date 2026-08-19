import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv("student_performance_ml.csv")

    plt.figure(figsize=(10, 6))
    plt.scatter(df["StudyHours"],df["PreviousScore"])
    plt.title("Distribution of Study Hours")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()