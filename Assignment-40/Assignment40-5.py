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

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

correct_predictions = (y_test.to_numpy() == y_pred).sum()
manual_accuracy = correct_predictions / len(y_test)
sklearn_accuracy = accuracy_score(y_test, y_pred)

print("Correct predictions:", correct_predictions)
print("Total test predictions:", len(y_test))
print("Manual accuracy:", manual_accuracy * 100, "%")
print("Sklearn accuracy:", sklearn_accuracy * 100, "%")
print("Both accuracy values match:", manual_accuracy == sklearn_accuracy)