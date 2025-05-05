import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")

#data1 = data.drop('variety')
data.hist(edgecolor = 'black', linewidth = 1.2)

fig = plt.gcf()
fig.set_size_inches(12, 12)

plt.show()
