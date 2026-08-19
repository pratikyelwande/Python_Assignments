import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv("student_performance_ml.csv")

    sns.countplot(
        x="SleepHours",
        hue="FinalResult",
        data=df
        
    )

    plt.title("Sleep Hours vs Final Result")
    plt.xlabel("Sleep Hours")
    plt.ylabel("Number of Students")
    plt.legend(title="Final Result", labels=["Fail", "Pass"])
    plt.show()


if __name__ == "__main__":
    main()