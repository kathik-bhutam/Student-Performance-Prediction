# Student Performance Prediction 📚

## 📌 Project Overview
Student Performance Prediction is a Machine Learning project that predicts a student's final marks based on academic performance and study-related factors.

The project uses **Linear Regression** to estimate final marks and provides an interactive web interface using Streamlit.

## 🎯 Problem Statement
The goal is to understand how factors such as study hours, attendance, previous marks, and assignment scores relate to students' final academic performance.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

## 📊 Dataset Information
The project uses a small fictional dataset containing the following features:

| Feature | Description |
|---|---|
| Study Hours | Hours spent studying |
| Attendance | Attendance percentage |
| Previous Marks | Marks obtained previously |
| Assignment Score | Assignment marks |
| Final Marks | Target variable to predict |

## 🖥️ Application Screenshot

![Student Performance Prediction App](screenshots/app_screenshot.png)

## 🤖 Machine Learning Algorithm
**Linear Regression**

The model learns relationships between the input features and final marks using training data.

## ✨ Features
- Predicts student final marks.
- Uses four academic input features.
- Trains a Linear Regression model.
- Saves the trained model.
- Provides an interactive Streamlit interface.

## 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── dataset/
│   ├── student_data.csv
│   └── cleaned_student_data.csv
│
├── models/
│   └── student_model.pkl
│
├── app.py
├── main.py
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kathik-bhutam/Student-Performance-Prediction.git
```

### 2. Open the project folder

```bash
cd Student-Performance-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the model (optional)

```bash
python train_model.py
```

### 5. Run the Streamlit application

```bash
python -m streamlit run app.py
```

## 📈 Output
The application displays predicted final marks based on the values entered by the user.

## ⚠️ Disclaimer
This is an educational project developed using a small fictional dataset. Predictions are for learning and demonstration purposes only and should not be used for actual academic decisions.

## 👨‍💻 Author
**karthik-bhutam**

GitHub: [karthik-bhutam](https://github.com/kathik-bhutam)
