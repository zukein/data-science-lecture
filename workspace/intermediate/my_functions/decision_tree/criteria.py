import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show(criteria):
    eps = np.finfo(np.float).eps
    x = np.linspace(eps, 1 - eps, 30)
    if criteria is 'gini':
        title = 'ジニ不純度'
        y = 1 - (x**2 + (1 - x)**2)
    elif criteria is 'entropy':
        title = 'エントロピー'
        y = -(x * np.log(x) + (1 - x) * np.log(1 - x))
    fig = plt.figure(figsize=figaspect(1))
    ax = fig.gca()
    ax.plot(x, y)
    ax.set(title=title, xlabel='一方のクラスの割合(全2クラス)', xlim=(0, 1), ylim=(0, 0.75))
    plt.show()
