import matplotlib .pylab as plt
import pandas as pd
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn import tree

housing = fetch_california_housing()
print(housing.DESCR)

print(housing.data.shape)

print(housing.data[0])

dtr = tree.DecisionTreeRegressor(max_depth=2)
dtr.fit(housing.data[:, [6, 7]], housing.target)
