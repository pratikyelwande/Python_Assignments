import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    df = pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"])
    Y = df["FinalResult"]
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    plt.figure(figsize=(10,6))
    plt.scatter(df["StudyHours"], df["FinalResult"], color='blue', label='Study Hours vs Final Result')
    plt.xlabel("Study Hours")
    plt.ylabel("Final Result")
    plt.title("Study Hours vs Final Result")
    plt.grid()
    plt.legend()
    plt.show()

    plt.figure(figsize=(10,6))
    plt.hist(df["StudyHours"], bins=10, color='grey', edgecolor='black')
    plt.xlabel("Study Hours")
    plt.ylabel("Frequency")
    plt.title("Distribution of Study Hours")
    plt.grid()
    plt.show()

    model = DecisionTreeClassifier()

    model = model.fit(x_train,y_train)

    print("Model trained Successfully")
    y_pred = model.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)
    print("Accuracy of the model is:", accuracy * 100, "%")
    cm = confusion_matrix(y_test,y_pred)
    print("Confusion Matrix:")
    print(cm)

    


if __name__ == "__main__":
    main()