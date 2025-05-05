import pandas as pd

df = pd.read_csv("INvideos.csv")

#[]<-- not required columns from csv mention here
df = df.drop([], axis = 1)

#[] <-- required column name mention here to change its data type as intger
df[[]] = df[[]].astype(int)

#[] <-- mention respective column name to find its count
views = df[].sum()
likes = df[].sum()
dislikes = df[].sum()
comments = df[].sum()

print("\nTotal Views : ", views)
print("\nTotal Likes : ", likes)
print("\nTotal Dislikes : ", dislikes)
print("\nTotal Comments : ", comments)

