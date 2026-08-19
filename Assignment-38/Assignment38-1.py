import pandas as pd

def main():
    df = pd.read_csv("student_performance_ml.csv")
    print("First 5 Records:")
    print(df.head(5))
    print("Last 5 Records:")
    print(df.tail(5))
    print("Total Records:")
    print(df.shape)
    print("List of Columns:")
    print(df.columns)
    print("Data Types of columns :")
    print(df.dtypes)

if __name__ == "__main__":
    main()