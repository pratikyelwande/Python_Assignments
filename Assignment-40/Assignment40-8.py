from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


DataPath = Path(__file__).with_name("student_performance_ml.csv")
FeatureColumns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

df = pd.read_csv(DataPath)
X = df[FeatureColumns]
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

root_feature = FeatureColumns[model.tree_.feature[0]]
print("Feature at the root node:", root_feature)
print("The root feature was selected first because it gives the greatest impurity reduction")
print("at the first split of the training data.")

plt.figure(figsize=(18, 10))
plot_tree(
    model,
    feature_names=FeatureColumns,
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True,
)
plt.title("Decision Tree for Student Performance")
plt.show()