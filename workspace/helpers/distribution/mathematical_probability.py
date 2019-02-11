import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    xticks = np.arange(1, 7)
    p = 1 / 6
    ax.vlines(xticks, 0, p, color='blue')
    ax.axhline(p, linestyle='dashed', color='gray')
    ax.set(
        title='サイコロの目の確率',
        xlabel='取りうる値',
        xticks=xticks,
        yticks=[p],
        yticklabels=[r'$\frac{1}{6}$'],
        ylim=(0, p * 1.1))
    ax.set_ylabel('確率', rotation=0, horizontalalignment='right')
    for label in ax.yaxis.get_ticklabels():
        label.set(size=label.get_size() * np.sqrt(2))
    plt.show()
