import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")
    print("Total number of Students :",len(df))
    passed=0
    failed=0
    for i in range(len(df)):
        if df['FinalResult'].iloc[i] == 1 :
            passed+=1
        else:
            failed+=1
    print("Total number of students passed:",passed)
    print("Total number of students failed:",failed)

    

if __name__ == "__main__":
    main()