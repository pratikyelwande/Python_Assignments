from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
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

matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(matrix)
print("\nTrue Positive: Actual Pass and predicted Pass.")
print("True Negative: Actual Fail and predicted Fail.")
print("False Positive: Actual Fail but predicted Pass.")
print("False Negative: Actual Pass but predicted Fail.")

display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=["Fail", "Pass"])
display.plot(cmap="Blues")
plt.title("Confusion Matrix")
plt.show()