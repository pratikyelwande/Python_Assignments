from pathlib import Path

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


DataPath = Path(__file__).with_name("student_performance_ml.csv")
BaseColumns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]

df = pd.read_csv(DataPath)
df["PerformanceIndex"] = (df["StudyHours"] * 2) + df["Attendance"]
FeatureColumns = BaseColumns + ["PerformanceIndex"]
X = df[FeatureColumns]
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)
accuracy = accuracy_score(y_test, model.predict(X_test))

print("New DataFrame columns:", FeatureColumns)
print("Accuracy with PerformanceIndex:", accuracy * 100, "%")
print("PerformanceIndex combines StudyHours and Attendance into one additional feature.")
print("Compare this accuracy with the full-feature model to decide whether accuracy improved.")