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
    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    y_train_pred = model.predict(x_train)

    training_accuracy = accuracy_score(y_train, y_train_pred)
    testing_accuracy = accuracy_score(y_test, y_pred)

    print("Training Accuracy:", training_accuracy * 100, "%")
    print("Testing Accuracy :", testing_accuracy * 100, "%")
if __name__ == "__main__":
    main()