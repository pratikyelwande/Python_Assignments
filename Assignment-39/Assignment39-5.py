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
training_accuracy = accuracy_score(y_train, model.predict(X_train))
testing_accuracy = accuracy_score(y_test, model.predict(X_test))

print(f"Training accuracy: {training_accuracy * 100:.2f}%")
print(f"Testing accuracy: {testing_accuracy * 100:.2f}%")
if training_accuracy > testing_accuracy + 0.10:
    print("Observation: The large gap suggests that the model is overfitting.")
elif training_accuracy < testing_accuracy:
    print("Observation: The model may be underfitting the training data.")
else:
    print("Observation: Training and testing accuracy are close, so there is no clear overfitting.")