# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 10:00:14 2019

@author: Joseph
"""

# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv("Data.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Taking care of missing data: Not needed in template
from sklearn.preprocessing import SimpleImputer
missingvalues = SimpleImputer(missing_values=np.nan, strategy="mean", verbose=0)
missingvalues = missingvalues.fit(X[:, 1:])
X[:, 1:] = missingvalues.transform(X[:, 1:])

# Encoding Categorical Data: Not needed in template
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X), dtype=np.float)

from sklearn.preprocessing import LabelEncoder
y = LabelEncoder().fit_transform(y)

# Splitting data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# Feature Scaling
"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""