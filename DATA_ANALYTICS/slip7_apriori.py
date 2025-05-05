import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

csv = pd.read_csv("Market_Basket_analysis.csv", header = None)

csv.dropna()

encoder = TransactionEncoder()
array = encoder.fit_transform(csv.values)

df = pd.DataFrame(array)

frequent = apriori(df, min_support = 0.01)
rule = association_rules(frequent)

print("\nOriginal Dataset : \n")
print(df.head())

print("\nFrequent Itemset : \n")
print(frequent)

print("\nAssociation Rules : \n")
print(rule)


