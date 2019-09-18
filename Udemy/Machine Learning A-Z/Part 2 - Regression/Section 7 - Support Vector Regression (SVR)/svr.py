# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 13:55:29 2019

@author: Joseph
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(np.reshape(y, (-1, 1)))

# Fitting SVR to the dataset
from sklearn.svm import SVR
regressor = SVR(kernel="rbf")
regressor.fit(X,y)

y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color="blue")
plt.title("SVR")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

