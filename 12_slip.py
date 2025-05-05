import pandas as pd
import numpy as np

data = {
        'Salary' : [10000, 20000, 30000, 10000, np.nan, 60000, 20000, 20000, 10000, 10000],
        'Department' : ["C", "DSA", "C++", "JAVA", np.nan, "WEB-Technology", "DSA", "DSA", "C", "C"]
        }

data1 = pd.DataFrame(data)

print("Original DataFrame : ")
print(data1)

data2 = data1.dropna()
data3 = data2.drop_duplicates(subset = None, keep = 'first', inplace = False)

print("Modified DataFrame")
print(data3)
