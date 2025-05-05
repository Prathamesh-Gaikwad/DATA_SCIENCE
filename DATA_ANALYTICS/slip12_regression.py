import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

data = {'Height' : [170, 10, 10],
        'Weight' : [70, 5, 10]
        }

df = pd.DataFrame(data)

x = df[['Height', 'Weight']].values
y = df.iloc[:, 1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 42)

regressor = LinearRegression()

regressor.fit(x_train, y_train)		#fitting dataset into model

y_pred = regressor.predict(x_test)
print("\nPredictions : ", y_pred)

mean = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error : ", mean)
