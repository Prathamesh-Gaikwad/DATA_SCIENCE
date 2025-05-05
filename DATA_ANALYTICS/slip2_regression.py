import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = {'Level' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Salary' : [15000, 30000, 60000, 90000, 120000, 160000, 180000, 200000, 240000, 280000]
        }

df = pd.DataFrame(data)

x = df[['Level', 'Salary']].values 
y = df.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

print("x_train : \n", x_train)
print("x_test : \n", x_test)
print("y_train : \n", y_train)
print("y_test : \n", y_test)

regressor = LinearRegression()

regressor.fit(x_train, y_train)		#fitting dataset into model

y_pred = regressor.predict(x_test)

mean = mean_squared_error(y_test, y_pred)

r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error : ", mean)
print("\nR2 Score : ", r2)

