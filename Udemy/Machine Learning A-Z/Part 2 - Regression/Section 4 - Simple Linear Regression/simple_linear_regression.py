# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:47:17 2019

@author: Joseph
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import dataset
dataset = pd.read_csv("Salary_Data.csv")
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Fitting Simple Linear Regression to Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualizing the Training set results
plt.scatter(X_train, y_train, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary vs Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

# Visualizing the Test set results
plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylable("Salary")
plt.show()