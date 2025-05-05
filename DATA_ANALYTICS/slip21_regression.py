import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv("user_data.csv")

df.dropna(inplace = True)

x = df['staff_rating'].values.reshape(-1, 1)
y = df['comfort_rating'].values.reshape(-1, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)

regressor = LinearRegression()

regressor.fit(x_train, y_train)		#fitting dataset into model

y_pred = regressor.predict(x_test)

mean = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error : ", mean)
print("\nR2 Score : ", r2)

plt.scatter(x_test, y_test, color = 'gray')
plt.plot(x_test, y_pred, color = 'red', linewidth = 2)
plt.show()
