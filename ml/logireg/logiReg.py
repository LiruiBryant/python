import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = 'data' + os.sep + "LogiReg_data.txt"
pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
print(pdData.head())


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def model(X, theta):
    return sigmoid(np.dot(X, theta.T))


pdData.insert(0, 'Ones', 1)
orig_data = pdData.as_matrix()
cols = orig_data.shape[1]
x = orig_data[:, 0, cols - 1]
y = orig_data[:, cols - 1:cols]

theta = np.zeros(1, 3)


def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
