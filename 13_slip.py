import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")

plt.figure(figsize = (8, 6))
plt.scatter(data['petal.length'], data['petal.width'], color = 'orange')

plt.title("Relationship Between Petal Length & Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
