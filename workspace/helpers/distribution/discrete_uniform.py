import numpy as np
from ipywidgets import interact, IntRangeSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

events = np.arange(-5, 11)
xlim = (events[0] - 1, events[-1] + 1)


def plot(int_range):
    x_min, x_max = int_range
    x = np.arange(x_min, x_max + 1)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    ax.vlines(x, 0, 1.0 / x.size)
    ax.set(title='離散一様分布', xlabel='取りうる値', xlim=xlim, ylim=(0, 1.1), xticks=x)
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    plt.show()


def show():
    interact(
        plot,
        int_range=IntRangeSlider(
            value=[1, 6],
            min=events[0],
            max=events[-1],
            step=1,
            description='$事象の範囲$：',
            continuous_update=False))
