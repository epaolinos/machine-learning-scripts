#Hey everyone, my name is Pavel Egizaryan, and this is my Data Science homework (4 September 2019)

import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

values = pd.read_csv("USD_CURRENCY_HISTORY.csv", sep = ",")["curs"]

past = 7 * 4 #four weeks of history for every point
future = 7 #one week of future for every point

start = past
end = len(values) - future
raw_df = []

for i in range(start, end):
    past_and_future_value = values[(i - past):(i + future)]
    raw_df.append(list(past_and_future_value))

past_columns = [f"past_{i}" for i in range(past)]
future_columns = [f"future_{i}" for i in range(future)]

df = pd.DataFrame(raw_df, columns = (past_columns + future_columns))

X = df[past_columns][:-1]
y = df[future_columns][:-1]

X_test = df[past_columns][-1:]  #one of past numbers for making a prediction
y_test = df[future_columns][-1:] #one of future numbers for the test of the prediction

from sklearn.neural_network import MLPRegressor

MLP = MLPRegressor(max_iter = 10000, tol = 0) #object of the MLPRegressor
#no idea how these parameters influence the prediction, I always get different results between 0.2 and 1.2

MLP.fit(X, y)

prediction = MLP.predict(X_test)[0]

plt.plot(prediction, label="prediction")
plt.plot(y_test.iloc[0], label="real")
plt.legend()

sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))

from sklearn.dummy import DummyRegressor

DR = DummyRegressor(strategy = 'median')

DR.fit(X, y)

prediction = DR.predict(X_test)[0]

plt.plot(prediction, label="prediction")
plt.plot(y_test.iloc[0], label="real")
plt.legend()

sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
#quite good result!
#it's joke, I was not about to use this fake regressor

from sklearn.kernel_ridge import KernelRidge

KR = KernelRidge(kernel='polynomial', coef0=1, degree=1) 
#coef0 and degree influence only polynomial kernel, not linear which is default

KR.fit(X, y)

prediction = KR.predict(X_test)[0]

plt.plot(prediction, label="prediction")
plt.plot(y_test.iloc[0], label="real")
plt.legend()

sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))

from sklearn.ensemble import RandomForestRegressor

FR = RandomForestRegressor(bootstrap=False)
#when bootstrap=False the whole dataset is used to build each tree

FR.fit(X, y)

prediction = FR.predict(X_test)[0]

plt.plot(prediction, label="prediction")
plt.plot(y_test.iloc[0], label="real")
plt.legend()

sklearn.metrics.mean_absolute_error(np.array([list(y_test.iloc[0])]), np.array([prediction]))
#this regressor doesn't change results very much if no parameter changed