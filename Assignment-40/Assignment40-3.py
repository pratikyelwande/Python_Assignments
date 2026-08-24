import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    df= pd.read_csv("student_performance_ml.csv")
    X = df[["StudyHours","Attendance"]]
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy_full= accuracy_score(y_test,y_pred)
    print("Accuracy of the model is :",accuracy_full*100,"%")
    X = df.drop(columns=["FinalResult"],axis=1)
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    
    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy= accuracy_score(y_test,y_pred)
    if accuracy == accuracy_full:
        print("Removing sleephours did not affect the accuracy")
    elif accuracy > accuracy_full:
        print("Removing sleephours improved the accuracy")
if __name__ == "__main__":
    main()