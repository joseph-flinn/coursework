# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 12:47:16 2019

@author: Joseph
"""

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv("Position_Salaries.csv")
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values

"""
# Splitting data 
# Not needed in this case (just making a formula?)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
"""

# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression().fit(X, y)

# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression().fit(X_poly, y)


# Visualizing both regression results
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color="red")
plt.plot(X, lin_reg.predict(X), color="blue")
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color="green")
plt.title("Linear Regression & Polynomial Regression")
plt.xlabel("Level")
plt.ylabel("Salary")
plt.show()

# Predicting a new result with Linear Regression
lin_reg.predict([[6.5]])
# Predicting a new result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform([[6.5]]))


