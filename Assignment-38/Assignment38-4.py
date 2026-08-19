import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")
    res_c = df["FinalResult"].value_counts() 

    result_counts = df["FinalResult"].value_counts(normalize=True) * 100
    print("Count of students based on Final Result:")
    print(res_c)
    print(f"Percentage ofstudents based on Final Result:")
    print(result_counts)
if __name__ == "__main__":
    main()