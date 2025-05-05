import pandas as pd
import numpy as np

df = pd.read_csv("Data.csv")

print("Data Frame : with missing values..")
print("======================================")
print(df)

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("Data Frame : without missing values..")
print("======================================")
print(df)
