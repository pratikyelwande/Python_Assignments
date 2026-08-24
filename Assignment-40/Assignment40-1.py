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
    importance = model.feature_importances_
    print("Feature Importances:", importance)
    for feature, score in zip(X.columns,importance):
        print(f"{feature}:{score}")
    print("Most important feature : ", importance.argmax())
    print("Least important feature : ", importance.argmin())
    print("Most important feature :",X.columns[importance.argmax()])
    print("Least important feature :",X.columns[importance.argmin()])
    y_pred = model.predict(x_test)
    
    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy of the model is:", accuracy * 100, "%")

if __name__ == "__main__":
    main()