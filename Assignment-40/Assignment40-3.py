from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


DataPath = Path(__file__).with_name("student_performance_ml.csv")
FullColumns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]
SelectedColumns = ["StudyHours", "Attendance"]

df = pd.read_csv(DataPath)
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(
    df, y, test_size=0.2, random_state=42, stratify=y
)

full_model = DecisionTreeClassifier(max_depth=5, random_state=42)
full_model.fit(X_train[FullColumns], y_train)
full_accuracy = accuracy_score(y_test, full_model.predict(X_test[FullColumns]))

selected_model = DecisionTreeClassifier(max_depth=5, random_state=42)
selected_model.fit(X_train[SelectedColumns], y_train)
selected_accuracy = accuracy_score(y_test, selected_model.predict(X_test[SelectedColumns]))

print("Full-feature model accuracy:", full_accuracy * 100, "%")
print("StudyHours and Attendance model accuracy:", selected_accuracy * 100, "%")
print("Accuracy difference:", (selected_accuracy - full_accuracy) * 100, "percentage points")
print("The two-feature model is still performing well if its accuracy remains close to the full model.")