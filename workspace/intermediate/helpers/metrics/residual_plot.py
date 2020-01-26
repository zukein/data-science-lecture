import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    np.random.seed(1234)
    x = np.random.uniform(-2, 2, size=(100, 1))
    y = x**3 + np.random.normal(size=x.shape)
    y_hat = LinearRegression().fit(x, y).predict(x)
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(y_hat, y - y_hat)
    ax.set(xticks=(), yticks=(), xlabel=r'$\hat{y}$', ylabel=r'$y-\hat{y}$')
    plt.show()
