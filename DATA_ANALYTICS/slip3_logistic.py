import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
        'User ID' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Gender' : [1, 1, 0, 0, 1, 1, 0, 0, 1, 0],
        'Age' : [19, 35, 26, 27, 19, 27, 32, 25, 33, 45],
        'Estimated Salary' : [15000, 30000, 60000, 90000, 120000, 160000, 180000, 200000, 240000, 280000],
        'Purchased' : [0, 0, 0, 1, 1, 0, 1, 0, 1, 1]
    }

df = pd.DataFrame(data)

x = df[['Gender', 'Purchased']].values
y = df.iloc[:, 4].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.5, random_state = 0)

regressor = LogisticRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)
print(y_pred)

score = accuracy_score(y_test, y_pred)
print(score)
