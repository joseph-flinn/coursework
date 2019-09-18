# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:41:55 2019

@author: Joseph

Linear Regression Assumptions:
    - Linearity
    - Homoscedasticity
    - Multivariate normality
    - Independence of errors
    - Lack of multicollinearity
        + Include only n-1 of the dummy variables
        
Methods of building models (There is a PDF of this in the notes)
1. All-in
    - Prior Knowledge (domain knowledge)
    - You have to
    - Preparing for Backward Elimination
2. Backward Elimination
    - Select a significance level to stay in the model (SL = 0.05)
    - Fit the full model with all possible predictors
    - Consider the predictor with the highest P-value. If P > SL, go to STEP 4, otherwise go to FIN
    - Remove the predictor
    - Fit model with this variable*
3. Forward Selection
    - Select a significance level to enter in the model (SL = 0.05)
    - Fit all simple regression models y ~ xn. Select the one with the lowest P-value
    - Keep this variable and fit all possible models with one extra predictor added to the one(s) you already have
    - Consider the predictor with the lowest P-value. If P < SL, go to STEP 3, otherwise go to FIN
    - FIN: Keep the previous model
4. Bidirectional Elimination (Stepwise Regression)
    - Select a significance level to enter and to stay in the model (SLENTER = 0.05, SLSTAY = 0.05)
    - Perform the next step of Forward Selection (new variables must have P < SLENTER to enter)
    - Perform ALL steps of Backward Elimination (old variables must have P < SLSTAY to stay)
    - No new variables can enter and no new variables can exit, your model is ready
5. Score Comparison
    - Select a criterion of goodness
    - Construct ALL possible Regression Models...
    - Select the one with the best criterion
"""

# Preprocessing
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("50_Startups.csv")
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

# OneHotEncoding categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer([('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)

# Avoiding the Dummy Variable Trap
X = X[:, 1:] # python library does this for us

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



# Fitting Multiple Linear Regression to the Training ste
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.api as sm # doesn't take into account the constant
X = np.append(arr=np.ones((50, 1)).astype(int), values=X, axis=1)
X_opt = X[:, [0,1,2,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0,1,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0,3,4,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0,3,5]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()
X_opt = X[:, [0,3]]
regressor_ols = sm.OLS(endog=y, exog=X_opt).fit()
regressor_ols.summary()

"""
def backwardElimination(x, SL):
    numVars = len(x[0])
    temp = np.zeros((50,6)).astype(int)
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        adjR_before = regressor_OLS.rsquared_adj.astype(float)
        if maxVar > SL:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    temp[:,j] = x[:, j]
                    x = np.delete(x, j, 1)
                    tmp_regressor = sm.OLS(y, x).fit()
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)
                    if (adjR_before >= adjR_after):
                        x_rollback = np.hstack((x, temp[:,[0,j]]))
                        x_rollback = np.delete(x_rollback, j, 1)
                        print (regressor_OLS.summary())
                        return x_rollback
                    else:
                        continue
    regressor_OLS.summary()
    return x
"""