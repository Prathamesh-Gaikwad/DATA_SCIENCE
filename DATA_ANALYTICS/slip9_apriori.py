import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transaction = [
                ['item1', 'item2', 'item3'],
                ['item2', 'item3'],
                ['item1', 'item2', 'item4'],
                ['item1', 'item4'],
                ['item2', 'item3', 'item4'],
                ['item1', 'item3', 'item4'],
                ['item1', 'item2'],
                ['item1', 'item3'],
                ['item3', 'item4'],
                ['item2', 'item4']
    ]

encoder = TransactionEncoder()
array = encoder.fit_transform(transaction)

df = pd.DataFrame(array)

frequent = apriori(df, min_support = 0.01)
rule = association_rules(frequent, metric = "lift")

print("\nFrequent Itemset : \n")
print(frequent)

print("\nAssociation Rules : \n")
print(rule)


