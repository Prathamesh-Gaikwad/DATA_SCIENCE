import pandas as pd

data = pd.read_csv("iris.csv")

print("--------DATA DESCRIPTION--------")
print(data.describe())
