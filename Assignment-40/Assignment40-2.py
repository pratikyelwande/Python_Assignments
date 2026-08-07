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

full_model = DecisionTreeClassifier(max_depth=5, random_state=42)
full_model.fit(X_train, y_train)
full_accuracy = accuracy_score(y_test, full_model.predict(X_test))

reduced_columns = [column for column in FeatureColumns if column != "SleepHours"]
reduced_model = DecisionTreeClassifier(max_depth=5, random_state=42)
reduced_model.fit(X_train[reduced_columns], y_train)
reduced_accuracy = accuracy_score(y_test, reduced_model.predict(X_test[reduced_columns]))

print("Accuracy with all features:", full_accuracy * 100, "%")
print("Accuracy without SleepHours:", reduced_accuracy * 100, "%")
print("Accuracy difference:", (reduced_accuracy - full_accuracy) * 100, "percentage points")
print("Removing SleepHours affects performance:", full_accuracy != reduced_accuracy)