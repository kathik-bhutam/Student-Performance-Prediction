import os
import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("dataset/cleaned_student_data.csv")

# Input features
X = data[[
    "study_hours",
    "attendance",
    "previous_marks",
    "assignment_score"
]]

# Target variable
y = data["final_marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict marks
predictions = model.predict(X_test)

# Evaluate model
error = mean_absolute_error(y_test, predictions)

print("Actual Marks:", list(y_test))
print("Predicted Marks:", predictions.round(2))
print("Mean Absolute Error:", round(error, 2))


os.makedirs("models", exist_ok=True)
# Save trained model
joblib.dump(model, "models/student_model.pkl")

print("Model saved successfully!")

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Actual Marks:", list(y_test))
print("Predicted Marks:", predictions.round(2))
print("Mean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# Compare actual and predicted marks

plt.scatter(y_test, predictions)

plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual vs Predicted Marks")

plt.show()