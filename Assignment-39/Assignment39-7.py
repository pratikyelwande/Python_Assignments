import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
def main():
    df = pd.read_csv("student_performance_ml.csv")
    X= df.drop(columns=["FinalResult"])
    Y= df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model1 = DecisionTreeClassifier(max_depth=1)

    model1 = model1.fit(x_train,y_train)
    y_pred1 = model1.predict(x_test)

    newdata =[[6,85,66,7,7]]
    prediction = model1.predict(newdata)
    print("Prediction for new data:", prediction)

    if prediction[0] == 1:
        print("The student is passed.")
    else:
        print("The student is failed.")

if __name__ == "__main__":
    main()