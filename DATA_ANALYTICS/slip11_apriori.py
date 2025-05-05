import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

TID = {
        1 : ["Butter", "Bread", "Milk"],
        2 : ["Butter", "Flour", "Milk", "Sugar"],
        3 : ["Butter", "Eggs", "Milk", "Salt"],
        4 : ["Eggs"],
        5 : ["Butter", "Flour", "Milk", "Salt"]
    }

transaction = []

for key, value in TID.items():
    transaction.append(value)

encoder = TransactionEncoder()
array = encoder.fit_transform(transaction)

df = pd.DataFrame(array)

support = [0.2, 0.4]

for Min in support:
    frequent = apriori(df, min_support = Min)
    rule = association_rules(frequent)

    print("\nMinimum Support : ", Min)
    print("\nFrequent Itemset : \n")
    print(frequent)
    print("\nAssociation Rules : ")
    print(rule)

