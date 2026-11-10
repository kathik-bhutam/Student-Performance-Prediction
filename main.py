import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("dataset/student_data.csv")

print(data)
print("\nFirst 5 records:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nStatistical summary:")
print(data.describe())

# Number of rows and columns
print("Dataset shape:", data.shape)

# Column names
print("\nColumn names:")
print(data.columns)

print("\nMissing values:")
print(data.isnull().sum())
print("\nDuplicate records:")
print(data.duplicated().sum())

cleaned_data = data.drop_duplicates()

print("Original records:", len(data))
print("After removing duplicates:", len(cleaned_data))

cleaned_data = cleaned_data.copy()

cleaned_data = cleaned_data.fillna(
    cleaned_data.median(numeric_only=True)
)

print("\nMissing values after cleaning:")
print(cleaned_data.isnull().sum())

cleaned_data.to_csv("dataset/cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved successfully!")


plt.scatter(data["study_hours"], data["final_marks"])

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.show()

#line plot
plt.plot(data["study_hours"], data["final_marks"], marker="o")

plt.xlabel("Study Hours")
plt.ylabel("Final Marks")
plt.title("Study Hours vs Final Marks")

plt.show()

# histgrome plot
plt.hist(data["final_marks"], bins=5)

plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Final Marks")

plt.show()

# bar plot
average_marks = data.groupby("attendance")["final_marks"].mean()

average_marks.plot(kind="bar")

plt.xlabel("Attendance")
plt.ylabel("Average Final Marks")
plt.title("Attendance vs Average Marks")

plt.show()