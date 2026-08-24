import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix


def main():
    df = pd.read_csv("WinePredictor.csv")
    print("First Records :")
    print(df.head())
    print("Null Values if any",df.isnull().sum())
    print("Describing Tables :")
    print(df.describe())

    X = df.drop(["Class"],axis=1)
    Y = df["Class"]

    x_train,x_test,y_train,y_test = train_test_split(X,Y, test_size=0.2,random_state=42)
    model = DecisionTreeClassifier()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    cm = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy :",accuracy *100)
    print("Confusion Matrix")
    print(cm)
if __name__ =="__main__":
    main()