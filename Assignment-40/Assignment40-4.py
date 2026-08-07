from pathlib import Path

import pandas as pd
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
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(df[FeatureColumns], df["FinalResult"])

new_students = pd.DataFrame(
    {
        "StudyHours": [2.0, 4.5, 6.0, 7.5, 9.0],
        "Attendance": [60, 75, 82, 90, 96],
        "PreviousScore": [45, 58, 68, 78, 88],
        "AssignmentsCompleted": [2, 4, 6, 8, 10],
        "SleepHours": [5, 6, 7, 8, 8],
    }
)
new_students["PredictedResult"] = model.predict(new_students[FeatureColumns])
new_students["PredictedResult"] = new_students["PredictedResult"].map({0: "Fail", 1: "Pass"})

print("Predictions for five new students:")
print(new_students.to_string(index=False))