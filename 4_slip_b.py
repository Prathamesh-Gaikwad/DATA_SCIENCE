import pandas as pd

data = pd.read_csv("Data.csv")

print("Keys Of Dataset :")
print("=================")
print(data.keys())

print("************************")

print("Number of Rows And Columns Of dataset :")
print("=================")
print(data.shape)

print("************************")

print("Description Of dataset :")
print("=================")
print(data.describe())

print("************************")

print("Type Of dataset :")
print("=================")
print(type(data))

print("************************")

print("First 10 Rows of dataset :")
print("=================")
print(data.head(10))

print("************************")

print("Last 3 Rows of dataset :")
print("=================")
print(data.tail(3))

print("Random 5 Records From Data Frame : ")
print(data.sample(5))
print("***********************************")
