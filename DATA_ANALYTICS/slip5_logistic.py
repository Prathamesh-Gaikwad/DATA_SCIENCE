import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns = iris.feature_names)

df['target'] = iris.target

print("\nStatistical Data Of Iris-Setosa : ")
print(df[df['target'] == 0].describe())

print("\nStatistical Data Of Iris-Versicolor : ")
print(df[df['target'] == 1].describe())

print("\nStatistical Data Of Iris-Virginica : ")
print(df[df['target'] == 2].describe())

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

regressor = LogisticRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Of Logistic Regression : ", accuracy)
