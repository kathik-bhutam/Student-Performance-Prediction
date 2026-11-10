import joblib
import pandas as pd

# Load saved model
model = joblib.load("models/student_model.pkl")

# New student information
new_student = pd.DataFrame([{
    "study_hours": 6,
    "attendance": 85,
    "previous_marks": 70,
    "assignment_score": 80
}])

# Predict final marks
prediction = model.predict(new_student)

print("Predicted Final Marks:", round(prediction[0], 2))