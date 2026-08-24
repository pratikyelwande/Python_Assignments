import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    df= pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"],axis=1)
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy_full= accuracy_score(y_test,y_pred)
    print("Accuracy of the model is :",accuracy_full*100,"%")

    new_students = pd.DataFrame({
    "StudyHours": [2, 5, 3, 7, 1],
    "Attendance": [60, 90, 75, 95, 50],
    "PreviousScore": [40, 80, 65, 90, 35],
    "AssignmentsCompleted": [3, 9, 6, 10, 2],
    "SleepHours": [7, 6, 8, 7, 5]
})
    predictions = model.predict(new_students)
    print("Predictions for new students:", predictions)
    for i ,pred in enumerate(predictions):
        result = "Pass" if pred == 1 else "Fail"
        print(f"Student {i+1}: {result}")
if __name__ == "__main__":
    main()