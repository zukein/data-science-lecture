import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    true_rate = 0.2
    x = np.linspace(0, 1, 50)
    pr = (1 - true_rate) * np.sqrt(1 - x**2) + true_rate

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    ax.fill_between(x, 0, pr, alpha=.1, label='PR-AUC')
    ax.plot(x, pr, label='PR曲線')
    ax.plot([0, 1, 1], [1, 1, 0], linestyle='--', label='完璧な分類器')
    ax.plot([0, 1], [true_rate] * 2, linestyle='--', label='ランダムな分類器')

    ax.legend(loc='center left')
    ax.grid()
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    ax.set(title='PR-AUC',
           xlabel='再現率',
           ylabel='適合率',
           xlim=(0, xlim[1]),
           ylim=(0, ylim[1]))

    plt.show()
