from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    x, y, a = make_regression(
        n_samples=8, n_features=1, noise=100, coef=True, random_state=1234)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.scatter(x, y, color='black', label='データ')
    xlim = ax.get_xlim()
    ax.plot(xlim, a * xlim, label='$y=ax+b$')
    ax.vlines(x, y, a * x, color='red', label='$y-\hat{y}$')
    ax.legend()
    ax.set(xlim=xlim, xticks=(), yticks=())
    plt.show()