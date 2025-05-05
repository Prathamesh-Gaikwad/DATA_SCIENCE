import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

name = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'class']
data = pd.read_csv("nursery.data", names = name)

x = data.drop('class', axis = 1)
y = data['class']

x = pd.get_dummies(x)
y = pd.get_dummies(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

print("\nTrainig Dataset (x_train, y_train) : \n", x_train, y_train)
print("\nTesting Dataset (x_test, y_test) : \n", x_test, y_test)

regressor = LinearRegression()

regressor.fit(x_train, y_train)		#fitting dataset into model

y_pred = regressor.predict(x_test)
print("\nPredictions : ", y_pred)

mean = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error : ", mean)

r2 = r2_score(y_test, y_pred)
print("\nR2 Score : ", r2)
