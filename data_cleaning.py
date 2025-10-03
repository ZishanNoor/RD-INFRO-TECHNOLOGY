import pandas as pd
import numpy as np
import random


file_path = "C:/Users/USER/OneDrive/Desktop/Data analysis/company1.csv"
try:
    data = pd.read_csv(file_path)
    print("--- 1. Data Loaded Successfully ---")
    print(data.head())
    print("\nInitial Missing Values (Before Cleaning):")
    print(data.isnull().sum())
    
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path.")
    exit()

print("\n--- 2. Handling Duplicates ---")
initial_rows = len(data)
data = data.drop_duplicates(subset=["EEID"], keep='first')
rows_removed = initial_rows - len(data)
print(f"Total Rows Removed (Duplicates): {rows_removed}")


mean_salary = data["salary"].mean()
data["salary"] = data["salary"].fillna(round(mean_salary, 2))
print(f"\n'salary' column: Imputed missing values with Mean Salary: {round(mean_salary, 2)}")


available_names = data["Name"].dropna().unique().tolist()
if not available_names:
    available_names = ["Zishan", "Aman", "Rohan", "Sohan"]

def impute_random_name(n):
    return random.choice(available_names)

data["Name"] = data["Name"].apply(lambda x: impute_random_name(x) if pd.isna(x) else x)
print("'Name' column: Imputed missing values with a Randomly Chosen Name.")


available_genders = data["gender"].dropna().unique().tolist()
if not available_genders:
    available_genders = ["M", "F", "Other"]

def impute_random_gender(g):
    return random.choice(available_genders)

data["gender"] = data["gender"].apply(lambda x: impute_random_gender(x) if pd.isna(x) else x)
print("'gender' column: Imputed missing values with a Randomly Chosen Gender.")


print("\n--- 4. Final Verification ---")
print("Final Missing Values (Should be zero for imputed columns):")
print(data.isnull().sum())

print("\nCleaned Data Head:")
print(data.head())


output_path = "C:/Users/USER/OneDrive/Desktop/Data analysis/company1_cleaned.csv"
data.to_csv(output_path, index=False)
print(f"\n--- 5. Cleaned Data Saved Successfully at: {output_path} ---")


print("\n--- Cleaning Summary ---")
print(f"Initial Rows: {initial_rows}")
print(f"Final Rows: {len(data)}")
print(f"Duplicates Removed: {rows_removed}")
print("Missing values handled: 'salary' → mean, 'Name' → random, 'gender' → random")
print("\n✅ Data Cleaning Completed Successfully!")
