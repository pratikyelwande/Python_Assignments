import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():

    df = pd.read_csv("student_performance_ml.csv")
    X= df.drop(columns=["FinalResult"])
    Y= df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier()

    model.fit(x_train,y_train)
    print("Model trained successfully!")
if __name__ == "__main__":
    main()