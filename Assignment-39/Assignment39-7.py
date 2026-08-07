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

new_student = pd.DataFrame(
    {
        "StudyHours": [6],
        "Attendance": [85],
        "PreviousScore": [66],
        "AssignmentsCompleted": [7],
        "SleepHours": [7],
    }
)
prediction = model.predict(new_student[FeatureColumns])[0]
result = "Pass" if prediction == 1 else "Fail"

print("New student details:")
print(new_student.to_string(index=False))
print("Predicted FinalResult:", prediction)
print("Prediction:", result)