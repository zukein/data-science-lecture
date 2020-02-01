import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect

resolution = 50


def show():
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=figaspect(2 / 1))

    distribution1 = stats.norm()
    x1 = np.linspace(-3, 3, resolution)
    thresh = 2
    left = np.linspace(x1.min(), -thresh, resolution)
    right = np.linspace(thresh, x1.max(), resolution)
    ax1.plot(x1, distribution1.pdf(x1), color='black')
    ax1.fill_between(left, 0, distribution1.pdf(left), color='red')
    ax1.fill_between(right, 0, distribution1.pdf(right), color='red')
    ax1.hlines(
        distribution1.pdf(thresh),
        x1.min(),
        thresh,
        linestyle='dashed',
        alpha=0.3)
    ax1.set(
        xlim=(x1.min(), x1.max()),
        ylim=(0, ax1.get_ylim()[1]),
        xticks=(-thresh, thresh),
        yticks=(),
        xticklabels=('', 'x'))

    total = 20
    n_objects = 8
    n_drawn = 8
    distribution2 = stats.hypergeom(total, n_objects, n_drawn)
    thresh = 5
    statistics = distribution2.pmf(thresh)
    x2 = np.arange(0, n_drawn + 1)
    y2 = distribution2.pmf(x2)
    left = (x2 <= thresh) & (y2 <= statistics)
    right = (x2 >= thresh) & (y2 <= statistics)
    center = ~left & ~right
    for interval, color in zip([left, center, right], ['red', 'black', 'red']):
        ax2.vlines(
            x2[interval], 0, distribution2.pmf(x2[interval]), color=color)
    ax2.hlines(
        distribution2.pmf(thresh),
        x1.min(),
        thresh,
        linestyle='dashed',
        alpha=0.3)
    ax2.set(
        xlim=(x2.min(), x2.max()),
        ylim=(0, ax2.get_ylim()[1]),
        xticks=(x2[left].max(), x2[right].min()),
        yticks=(),
        xticklabels=('', 'x'))

    plt.show()
