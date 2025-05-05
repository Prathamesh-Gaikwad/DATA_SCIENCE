
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.csv")
ax = plt.subplots(1, 1, figure = (10, 8))

iris['sepal.length'].value_counts().plot.pie(shadow = True, figsize = (10, 8))

plt.title("Iris species %")
plt.show()

