import numpy as np
from scipy import stats
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def plot(mean):
    x = np.arange(10)
    y = stats.poisson.pmf(x, mean)

    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, y)
    ax.set(
        title='ポアソン分布',
        xlabel=r'取りうる値 $\left( 0\sim \infty \right)$',
        ylim=(0, 1.1))
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    style = dict(description_width='initial')
    interact(
        plot,
        mean=FloatSlider(
            value=1.0,
            min=0.1,
            max=5.0,
            step=0.1,
            description=r'期待値 (平均) $( p\times n)$：',
            continuous_update=False,
            readout_format='.1f',
            style=style))
