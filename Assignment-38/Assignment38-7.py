import pandas as pd
import matplotlib.pyplot as plt
def main():
    df = pd.read_csv("student_performance_ml.csv")
    passed = df[df["FinalResult"]== 1]
    failed = df[df["FinalResult"]== 0]

    plt.figure(figsize=(10, 6))
    plt.scatter(passed["StudyHours"],passed["PreviousScore"],color="green",label="Passed")
    plt.scatter(failed["StudyHours"],failed["PreviousScore"],color="red",label="Failed")
    plt.title("study hours vs previous score")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.legend()
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()