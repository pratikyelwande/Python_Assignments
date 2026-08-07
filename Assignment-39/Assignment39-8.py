from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


# Step 1: Load the student performance dataset.
DataPath = Path(__file__).with_name("student_performance_ml.csv")
df = pd.read_csv(DataPath)

# Step 2: Analyze the data and display its basic structure.
FeatureColumns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
]
print("Dataset shape:", df.shape)
print("Column names:", list(df.columns))
print("FinalResult distribution:")
print(df["FinalResult"].value_counts())

# Step 3: Visualize the relationship between StudyHours and FinalResult.
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="FinalResult", y="StudyHours", hue="FinalResult", legend=False)
plt.title("Study Hours by Final Result")
plt.xlabel("Final result (0 = Fail, 1 = Pass)")
plt.ylabel("Study hours per day")
plt.show()

# Step 4: Separate input features and target, then split the dataset.
X = df[FeatureColumns]
y = df["FinalResult"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 5: Create and train the Decision Tree model.
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Step 6: Predict results for the test data.
y_pred = model.predict(X_test)
print("Predicted results:", y_pred)

# Step 7: Calculate and display model accuracy.
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy * 100:.2f}%")

# Step 8: Generate and display the confusion matrix.
matrix = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")
print(matrix)
ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=["Fail", "Pass"]).plot(cmap="Blues")
plt.title("Student Performance Confusion Matrix")
plt.show()

# Step 9: State a final conclusion based on the test result.
print("Conclusion: The Decision Tree uses academic and behavioral features to predict Pass or Fail.")
print("The testing accuracy and confusion matrix show how well it generalizes to unseen students.")