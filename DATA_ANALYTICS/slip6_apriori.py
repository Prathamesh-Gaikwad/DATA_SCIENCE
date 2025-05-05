import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

TID = {
        1 : ["Bread", "Milk"],
        2 : ["Bread", "Diaper", "Beer", "Eggs"],
        3 : ["milk", "Diaper", "Beer", "Coke"],
        4 : ["Bread", "Milk", "Diaper", "Beer"],
        5 : ["Bread", "Milk", "Diaper", "Coke"]
    }

transaction = []

for key, value in TID.items():
    transaction.append(value)

encoder = TransactionEncoder()
array = encoder.fit_transform(transaction)

df = pd.DataFrame(array)

support = [0.2, 0.4, 0.6]

for Min in support:
    frequent = apriori(df, min_support = Min)
    rule = association_rules(frequent)

    print("\nMinimum Support : ", Min)
    print("\nFrequent Itemset : \n")
    print(frequent)
    print("\nAssociation Rules : ")
    print(rule)

