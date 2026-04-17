"""
This program reads health_data.csv, adds BMI and Health_Status columns.
"""
import pandas as pd

# reading file
df = pd.read_csv("health_data.csv")

# calculating BMI
df["BMI"] = df["weight"] / df["height"]

# function to assign health status
def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Healthy"
    elif bmi <= 29.9:
        return "Overweight"
    elif bmi <= 34.9:
        return "High Risk"
    else:
        return "Critical"

# applying function
df["Health_Status"] = df["BMI"].apply(get_status)

print(df.head())