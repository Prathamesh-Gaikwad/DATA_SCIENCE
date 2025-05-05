import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

weight = []
for i in range(50):
    fish = []

    for j in range(7):
        no = random.randint(1, 20)
        fish.append(no)

    weight.append(fish)
    
df = pd.DataFrame(weight)

x = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

regressor = LinearRegression()

regressor.fit(x_train, y_train)		#fitting dataset into model

y_pred = regressor.predict(x_test)
print("\nWeight Prediction : ", y_pred)
