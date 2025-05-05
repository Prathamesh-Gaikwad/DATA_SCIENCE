import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("Data.csv")
x = data['Age']
y = data['Salary']

plt.plot(x, y)
plt.title("line plot of age vs salary")
plt.show()
