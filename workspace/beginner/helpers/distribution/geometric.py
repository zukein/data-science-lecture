import numpy as np
from scipy import stats
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(p):
    x = np.arange(1, 10)
    y = stats.geom.pmf(x, p)

    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, y)
    ax.set(
        title='幾何分布',
        xlabel=r'取りうる値 $\left( 0\sim \infty \right)$',
        ylim=(0, 1))
    ax.set_ylabel('確率密度', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    interact(
        plot,
        p=FloatSlider(
            value=0.5,
            min=0.1,
            max=1.0,
            step=0.1,
            description='確率／回',
            continuous_update=False,
            readout_format='.1f'))
