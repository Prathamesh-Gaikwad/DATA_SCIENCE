import pandas as pd
import numpy as np

data = pd.read_csv("weight-height.csv")

print("Dataset : ")
print(data)
print("======================")

print("Height Mean : ")
print(data['Height'].mean())

print("Height Median : ")
print(data['Height'].median())
print("======================")

print("Weight Mean : ")
print(data['Weight'].mean())

print("Weight Median : ")
print(data['Weight'].median())
print("======================")
