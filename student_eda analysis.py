# =====================================
# Student Performance EDA Project
# CodeAlpha Internship Task
# =====================================

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Sample Dataset
# -----------------------------
data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Rahul",
             "Sneha", "Vijay", "Meena", "Ajay", "Pooja"],
    "Age": [22, 21, 23, 22, 24, 21, 25, 22, 23, 24],
    "Gender": ["Male", "Female", "Male", "Female", "Male",
               "Female", "Male", "Female", "Male", "Female"],
    "Marks": [85, 92, 78, 88, 67, 95, 72, 90, 80, 86]
}

df = pd.DataFrame(data)

# -----------------------------
# Dataset Information
# -----------------------------
print("=" * 50)
print("STUDENT PERFORMANCE EDA")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Statistical Summary
# -----------------------------
print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Average Marks
# -----------------------------
average_marks = df["Marks"].mean()
print("\nAverage Marks:", round(average_marks, 2))

# -----------------------------
# Highest Scorer
# -----------------------------
highest = df[df["Marks"] == df["Marks"].max()]

print("\nHighest Scorer:")
print(highest)

# -----------------------------
# Marks Distribution
# -----------------------------
plt.figure(figsize=(6, 4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.savefig("output1_marks_distribution.png")
plt.show()

# -----------------------------
# Age Distribution
# -----------------------------
plt.figure(figsize=(8, 4))
plt.bar(df["Name"], df["Age"])
plt.title("Student Age Analysis")
plt.xlabel("Students")
plt.ylabel("Age")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output2_age_analysis.png")
plt.show()

# -----------------------------
# Gender Distribution
# -----------------------------
plt.figure(figsize=(5, 4))
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output3_gender_distribution.png")
plt.show()

print("\nEDA Completed Successfully!")
print("Charts saved as PNG files.")