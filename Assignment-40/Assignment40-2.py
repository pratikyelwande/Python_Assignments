import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    df= pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy_full = accuracy_score(y_test,y_pred)

    df.drop(columns=["SleepHours"], inplace= True)
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracywithoutsleep = accuracy_score(y_test,y_pred)
    if accuracywithoutsleep == accuracy_full:
        print("Removing sleephours did not affect the accuracy")
    elif accuracywithoutsleep > accuracy_full:
        print("Removing sleephours improved the accuracy")
    else:
        print("Removing sleephours reduced the accuracy")
if __name__ == "__main__":
    main()