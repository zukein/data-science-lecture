import numpy as np
from scipy import stats
from ipywidgets import interact, IntSlider, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

x_max = 10
xticks = np.arange(x_max + 1)


def plot(n, p):
    x = np.arange(n + 1)
    y = stats.binom.pmf(x, n, p)

    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, y)
    ax.set(
        title='二項分布',
        xlabel='取りうる値',
        xlim=(-1, x_max + 1),
        ylim=(0, 1.1),
        xticks=x)
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    interact(
        plot,
        n=IntSlider(
            value=3,
            min=1,
            max=x_max,
            step=1,
            description='回数：',
            continuous_update=False),
        p=FloatSlider(
            value=0.5,
            min=0.0,
            max=1.0,
            step=0.1,
            description='確率：',
            continuous_update=False,
            readout_format='.1f'))
