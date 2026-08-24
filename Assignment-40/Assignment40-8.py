import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
def main():
    df= pd.read_csv("student_performance_ml.csv")
    X = df.drop(columns=["FinalResult"],axis=1)
    Y = df["FinalResult"]

    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    model = DecisionTreeClassifier()
    model = model.fit(x_train,y_train)
    y_pred = model.predict(x_test)

    plt.figure(figsize=(15,10))
    plot_tree(model,feature_names=X.columns, class_names=["fail","pass"], filled=True)
    plt.show()

if __name__ == "__main__":
    main()