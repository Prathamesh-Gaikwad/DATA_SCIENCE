import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

data = {
        'No' : [1, 2, 3, 4],
        'Company' : ["Tata", "MG", "Kia", "Hyundia"],
        'Model' : ["Nexon", "Astor", "Seltos", "Creta"],
        'Year' : [2017, 2021, 2019, 2015]
    }
df = pd.DataFrame(data)

transactions = df[['Company', 'Model']].values.tolist()

encoder = TransactionEncoder()
array = encoder.fit_transform(transactions)

df = pd.DataFrame(array)

support = [0.1, 0.2]

for Min in support:
    frequent = apriori(df, min_support = Min)
    rule = association_rules(frequent)

    print("\nMinimum Support : ", Min)
    print("\nFrequent Itemset : \n")
    print(frequent)
    print("\nAssociation Rules : ")
    print(rule)
