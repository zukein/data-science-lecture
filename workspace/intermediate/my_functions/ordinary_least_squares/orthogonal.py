import matplotlib.pyplot as plt
from matplotlib.figure import figaspect


def show():
    plt.figure(figsize=figaspect(1))
    ax = plt.axes()
    arrowprop = dict(width=0.02, length_includes_head=True)
    yx, yy = 2, 2
    delta = 0.17
    ax.arrow(0, 0, 0.5, 0, **arrowprop)
    ax.annotate('$x$', (0, 0), (0.25, -delta))
    ax.arrow(0, 0, yx, 0, **arrowprop)
    ax.annotate('$\hat{y}$', (0, 0), (yx / 2, -delta))
    ax.arrow(0, 0, yx, yy, **arrowprop)
    ax.annotate('$y$', (0, 0), (yx / 2 - delta, yy / 2 + delta))
    ax.arrow(yx, 0, 0, yy, **arrowprop)
    ax.annotate('$e$', (0, 0), (yx + delta, yy / 2))
    ax.set(xlim=(-delta * 2, 2 + delta * 2),
           ylim=(-delta * 2, 2 + delta * 2),
           xticks=(),
           yticks=())
    plt.show()
