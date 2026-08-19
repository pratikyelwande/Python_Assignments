import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")
    print("Final result ")
    print(df.groupby("FinalResult")["StudyHours"].mean())
    print(df.groupby("FinalResult")["Attendance"].mean())

    """Students who passed generally have higher average StudyHours than students who failed.
    Students who passed generally have higher average Attendance than students who failed."""
if __name__ == "__main__":
    main()