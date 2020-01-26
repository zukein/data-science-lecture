import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from ipywidgets import interact, IntSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def f(x):
    return x * (x - 1) * (x + 1)


def noise_like(x):
    return np.random.normal(scale=0.3, size=x.shape)


def plot(k):
    np.random.seed(1234)
    x = np.linspace(-2, 2, 9).reshape((-1, 1))
    y = f(x) + noise_like(x)
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    ax.scatter(x, y, c='black', label='訓練データ')
    xlim = ax.get_xlim()
    xx = np.linspace(xlim[0], xlim[1], 100).reshape((-1, 1))
    ax.plot(xx, f(xx), linestyle='dashed', label='真の分布')
    ylim = ax.get_ylim()
    model = Pipeline([('transform', PolynomialFeatures(degree=k)),
                      ('linear', LinearRegression())])
    pred = model.fit(x, y).predict(xx)
    ax.plot(xx, pred, label='予測')
    ax.legend()
    ax.set(xlim=xlim, ylim=ylim, xticks=(), yticks=())
    plt.show()


def show():
    k = IntSlider(value=8,
                  min=1,
                  max=20,
                  description='モデルの複雑さ',
                  continuous_update=False,
                  style={'description_width': 'initial'})
    interact(plot, k=k)
