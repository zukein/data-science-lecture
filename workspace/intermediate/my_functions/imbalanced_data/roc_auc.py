import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    x = np.linspace(0, 1, 50)
    roc = np.sqrt(1 - (x - 1)**2)

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()

    ax.fill_between(x, 0, roc, alpha=.1, label='ROC-AUC')
    ax.plot(x, roc, label='ROC曲線')
    ax.plot([0, 0, 1], [0, 1, 1], linestyle='--', label='完璧な分類器')
    ax.plot([0, 1], [0, 1], linestyle='--', label='ランダムな分類器')

    ax.legend(loc='lower right')
    ax.grid()
    xlim, ylim = ax.get_xlim(), ax.get_ylim()
    ax.set(title='ROC-AUC',
           xlabel='偽陽性率',
           ylabel='真陽性率',
           xlim=(xlim[0], 1),
           ylim=(0, ylim[1]))

    plt.show()
