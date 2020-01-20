import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from ipywidgets import interact, IntSlider, fixed
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

resolution = 100


def plot(k, x, y):
    model = KNeighborsClassifier(n_neighbors=k).fit(x, y)
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k')
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    x_center, y_center = np.mean(xlim), np.mean(ylim)
    diff = max(xlim[1] - xlim[0], ylim[1] - ylim[0]) / 2
    xlim = (x_center - diff, x_center + diff)
    ylim = (y_center - diff, y_center + diff)
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], resolution),
                         np.linspace(ylim[0], ylim[1], resolution))
    grid = np.c_[xx.ravel(), yy.ravel()]
    pred = model.predict(grid)
    ax.pcolormesh(xx, yy, pred.reshape(xx.shape), alpha=0.2, edgecolors='none')
    ax.set(xlim=xlim, ylim=ylim, xticks=(), yticks=())
    plt.show()


def show(x, y):
    k = IntSlider(value=3,
                  min=1,
                  max=10,
                  description='k',
                  continuous_update=False)
    interact(plot, k=k, x=fixed(x), y=fixed(y))
