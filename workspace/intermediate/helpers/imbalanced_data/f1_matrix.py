import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    division = 10
    values = np.linspace(np.finfo(np.float).eps, 1, division)

    PRE = np.tile(values.reshape(1, -1), (division, 1))
    REC = np.tile(values.reshape(-1, 1), (1, division))
    F1 = 2 * (PRE * REC) / (PRE + REC)
    F1[0, 0] = np.nan

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.matshow(F1, cmap='Reds', alpha=0.6)
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    for (row, col), value in np.ndenumerate(F1):
        ax.text(x=col,
                y=row,
                s='{v:.2f}'.format(v=value),
                verticalalignment='center',
                horizontalalignment='center',
                size='small')

    ticks = np.arange(division)
    ticklabels = ['{:.1f}'.format(v) for v in values]
    ax.set(title='F1 score',
           xlim=xlim,
           ylim=ylim,
           xlabel='再現率 (Recall)',
           ylabel='適合率 (Precision)',
           xticks=ticks,
           yticks=ticks,
           xticklabels=ticklabels,
           yticklabels=ticklabels)
    for ticklabels in [ax.get_xticklabels(), ax.get_yticklabels()]:
        for text in ticklabels:
            text.set(size='small')

    plt.show()
