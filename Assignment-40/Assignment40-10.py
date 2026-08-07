from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


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

model = DecisionTreeClassifier(max_depth=None, random_state=42)
model.fit(X_train, y_train)
training_accuracy = accuracy_score(y_train, model.predict(X_train))
testing_accuracy = accuracy_score(y_test, model.predict(X_test))

print("Training accuracy:", training_accuracy * 100, "%")
print("Testing accuracy:", testing_accuracy * 100, "%")
print("A lower testing accuracy means the tree learned training-specific patterns that do not")
print("generalize to unseen data. This is called overfitting.")