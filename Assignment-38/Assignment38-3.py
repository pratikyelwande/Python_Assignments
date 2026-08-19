import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")

    print("Average studyhours of students :",df['StudyHours'].mean())
    print("Average Attendance of students :",df['Attendance'].mean())

    print("MAX Previous Score of students :",df['PreviousScore'].max())
    print("MIN SleepHours of students :",df['SleepHours'].min())

    

if __name__ == "__main__":
    main()