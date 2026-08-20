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
    accuracy = accuracy_score(y_test,y_pred1)
    print("Accuracy of Decision Tree Classifier with max_depth=1:", accuracy * 100, "%")

    model2 = DecisionTreeClassifier(max_depth=3)
    model2 = model2.fit(x_train,y_train)
    y_pred2 = model2.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred2)
    print("Accuracy of Decision Tree Classifier with max_depth=3:", accuracy * 100, "%")

    model3 = DecisionTreeClassifier()
    model3 = model3.fit(x_train,y_train)
    y_pred3 = model3.predict(x_test)
    accuracy = accuracy_score(y_test,y_pred3)
    print("Accuracy of Decision Tree Classifier with max_depth=3:", accuracy * 100, "%")

    
if __name__ == "__main__":
    main()