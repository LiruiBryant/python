import matplotlib.pylab as plt
import pandas as pd
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn import tree
from sklearn import tree
import pydotplus
import os
from IPython.display import Image

os.environ["PATH"] += os.pathsep + 'C:\Program Files (x86)\Graphviz2.38\\bin'

housing = fetch_california_housing()
print(housing.DESCR)

print(housing.data.shape)

print(housing.data[0])

dtr = tree.DecisionTreeRegressor(max_depth=2)
fit = dtr.fit(housing.data[:, [6, 7]], housing.target)
print(fit)

dot_data = \
    tree.export_graphviz(
        dtr,
        out_file=None,
        feature_names=housing.feature_names[6:8],
        filled=True,
        impurity=False,
        rounded=True
    )

graph = pydotplus.graph_from_dot_data(dot_data)
graph.get_nodes()[7].set_fillcolor("#FFF2DD")

Image(graph.create_png())

graph.write_png("dot.png")

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = \
    train_test_split(housing.data, housing.target, test_size=0.1, random_state=42)

dtr = tree.DecisionTreeRegressor(random_state=42)
dtr.fit(data_train, target_train)
print(dtr.score(data_test, target_test))

from sklearn.ensemble import RandomForestRegressor

rfr = RandomForestRegressor(random_state=42)
rfr.fit(data_train, target_train)
print(rfr.score())
