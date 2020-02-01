import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    titles = ['(1) 変数同士の独立を仮定', '(2) 変数同士に高い相関', '(3) 予測平面が定まらない']
    n = 100

    np.random.seed(1234)

    x1 = np.random.uniform(size=n)
    x2 = np.random.uniform(size=n)

    for i in range(3):
        fig = plt.figure(figsize=figaspect(1))
        fig.suptitle(titles[i])
        if i < 2:
            ax = fig.gca()
            ax.scatter(x1, x2 if i is 0 else x1, color='black')
            ax.set(xlabel='$x_{1}$', ylabel='$x_{2}$', xticks=(), yticks=())
        else:
            ax = Axes3D(fig, elev=10, azim=-70)
            xx, yy = np.meshgrid((0, 1), (0, 1))
            zz = (xx + yy) / 2
            ax.plot_surface(xx, yy, zz, color='red', alpha=0.6)
            ax.scatter(x1, x1, x1, color='black')
            ax.set(xlabel='$x_{1}$',
                   ylabel='$x_{2}$',
                   zlabel='$y$',
                   xlim=(0, 1),
                   ylim=(0, 1),
                   xticks=(),
                   yticks=(),
                   zticks=())

    plt.show()
