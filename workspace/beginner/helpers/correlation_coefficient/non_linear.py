import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    x = np.linspace(-1, 1, 9)
    y = x ** 2
    r = stats.pearsonr(x, y)[0]

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.scatter(x, y)
    ax.set(title=f'$y=x^{{2}}$の相関係数$r={r}$', xlabel='$X$',
           ylabel='$Y$', xticks=(), yticks=())

    plt.show()
