import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    eps = np.finfo(np.float).eps
    y_hat = np.linspace(eps, 1 - eps, 200)
    cost_pos = - np.log(y_hat)
    cost_neg = - np.log(1 - y_hat)

    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(y_hat, cost_pos, label='$y=1$')
    ax.plot(y_hat, cost_neg, label='$y=0$')
    ax.legend(loc='upper center')
    ax.set(title='クロスエントロピー', xlim=(0, 1),
             ylim=(0, 5), xlabel=r'$\hat{y}$',
             ylabel='コスト')

    plt.show()
