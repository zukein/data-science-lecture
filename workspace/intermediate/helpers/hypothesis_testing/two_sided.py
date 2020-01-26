import numpy as np
from scipy import stats
from ipywidgets import interact, FloatSlider
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

x_min, x_max = -3, 3
resolution = 50


def plot(alpha):
    distribution = stats.norm()
    range_min, range_max = distribution.interval(1 - alpha)
    left = np.linspace(x_min, range_min, resolution)
    center = np.linspace(range_min, range_max, resolution)
    right = np.linspace(range_max, x_max, resolution)
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    for xx, color, label in zip([left, center, right], ['red', 'blue', 'red'],
                                ['棄却域', '採択域', None]):
        ax.fill_between(xx, distribution.pdf(xx), color=color, label=label)
    ax.legend()
    ax.set(
        title='両側検定',
        xlim=(x_min, x_max),
        ylim=(0, ax.get_ylim()[1]),
        xticks=(),
        yticks=())
    plt.show()


def show():
    interact(
        plot,
        alpha=FloatSlider(
            value=0.05,
            min=0.01,
            max=0.3,
            step=0.01,
            description='有意水準',
            continuous_update=False,
            readout_format='.2f'))
