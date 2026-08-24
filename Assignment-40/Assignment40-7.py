import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    df= pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"],axis=1)
    Y = df["FinalResult"]
    random_states = [0,10,42]
    for state in random_states:
            x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=state)

            model = DecisionTreeClassifier()
            model = model.fit(x_train,y_train)
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test,y_pred)
            print("Testing accuracy is :",accuracy*100,"%")


if __name__ == "__main__":
    main()